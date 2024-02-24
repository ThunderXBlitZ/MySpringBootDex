import glob
import re
from typing import List, Dict
import os

import frontmatter

post_dir = 'docs/'
draft_dir = '_drafts/'
tag_dir = 'tag/'

INDEX_MD = "index.md"


def execute(include_drafts: bool) -> None:
    tags = crawl_pages(include_drafts)
    generate_tag_pages(tags)

def crawl_pages(include_drafts: bool) -> List[str]:
    '''
    Reads post_dir (and optionally, draft_dir), scans Front Matter
    Returns dictionary of tags and payloads
    '''

    files = glob.glob(post_dir + '**/*.md')

    if include_drafts:
        files = files + glob.glob(draft_dir + '*md')

    total_tags = {}
    for filepath in files:

        filename = filepath.split('/')[-1]
        if filename == INDEX_MD:
            continue

        payload = parse_md(filepath)
        total_tags = merge_dictionaries(total_tags, payload)
    
    return total_tags

def parse_md(filepath:str) -> Dict:
    ''' Returns Dict where tags are keys, and value is {about, relative_url} '''

    with open(filepath, 'r', encoding='utf8') as _f:
        metadata, content = frontmatter.parse(_f.read())
        tags = metadata.get('tags')
        if tags:
            title = metadata.get('title')
            relative_url = '/' + filepath.split('.')[0]
            about = extract_about_text(content)
            payload = {tag: {"about": about, "relative_url": relative_url} for tag in tags}
        else:
            payload = {}
    return payload

def extract_about_text(text: str) -> str:
    ''' Extract text in ### About section of md file '''

    text = text.replace('\n', '')
    pattern = re.compile(r'###\sAbout(.*?)\s*###', re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) >= 1:
        return matches[0].strip()
    else:
        return None

def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    ''' Aggregate dictionary, with values into lists '''

    merged_dict = {}
    
    keys = set(dict1.keys()) | set(dict2.keys())
    for key in keys:
        val1 = dict1.get(key, [])
        if not isinstance(val1, list):
            val1 = [val1]
        val2 = dict2.get(key, [])
        if not isinstance(val2, list):
            val2 = [val2]
        merged_dict[key] = val1 + val2
    return merged_dict

def generate_tag_pages(tags:List[Dict]) -> None:
    ''' Clear and re-create tag pages with the required content '''

    old_tags = glob.glob(tag_dir + '*.md')
    for filename in old_tags:
        if filename.split('/')[-1] != INDEX_MD:
            os.remove(filename)
        
    if not os.path.exists(tag_dir):
        os.makedirs(tag_dir)

    for tag, payloads in tags.items():
        tag_filename = tag_dir + tag.replace(' ', '_') + '.md'
        f = open(tag_filename, 'a')
        write_str = '---\nlayout: mydefault\ntitle: \"Tag: ' + tag + '"\nparent: "Tags"\n' + '\nrobots: noindex\n---\n'
        write_str += f"<h2>Tag: {tag}</h2>"
        write_str += "<div><ul>\n"
        for payload in payloads:
            write_str += "\t<li>\n"
            write_str += f"\t\t<a href=\'{payload.get('relative_url')}\'>{tag}</a>\n"
            write_str += f"\t\t<p>{payload.get('about')}</p>\n"
            write_str += "\t</li>\n"
        write_str += "</ul></div>"
        f.write(write_str)
        f.close()
    print("Tags generated, count", len(tags))


if __name__ == "__main__":
    include_drafts = os.getenv('include_drafts') or False
    execute(include_drafts)
