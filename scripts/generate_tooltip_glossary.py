# all pages -> about goes into glossary as key value pair
    # page title : about
# manual glossary + generated glossary = final glossary
# github action to generate generated and final glossary and commit

import glob
import re
from typing import List, Dict
import os

from utils import extract_about_text

import frontmatter
import yaml


manual_glossary_filepath = '_data/manual_glossary.yml'
glossary_filepath = '_data/glossary.yml'
base_url = "/MySpringBootDex"

post_dir = 'docs/'
draft_dir = '_drafts/'
tag_dir = 'tag/'

INDEX_MD = "index.md"


def execute(include_drafts: bool):
    data = crawl_pages(include_drafts)
    generate_auto_glossary(data)

def crawl_pages(include_drafts: bool) -> Dict:
    ''' Reads pages and extracts their title and about '''

    files = glob.glob(post_dir + '**/*.md')

    if include_drafts:
        files = files + glob.glob(draft_dir + '*md')

    glossary = {}
    for filepath in files:

        filename = filepath.split('/')[-1]
        if filename == INDEX_MD:
            continue

        payload = parse_md(filepath)
        glossary = {**payload, **glossary}
    
    return glossary

def parse_md(filepath:str) -> Dict:
    ''' For Annotation pages with title starting with '@',
    return key-value pair { title: {relative_url, about} } '''

    with open(filepath, 'r', encoding='utf8') as _f:
        metadata, content = frontmatter.parse(_f.read())
        title = metadata.get('title')
        if title[0] == '@':
            relative_url = base_url + '/' + filepath.split('.')[0]
            about = extract_about_text(content)
            return {title: {"about": about, "relative_url": relative_url}}
        else:
            return {}

def generate_auto_glossary(data: Dict) -> None:
    data = [{'term': x, 'definition': y['about'], 'url': y['relative_url']} for x,y in data.items()]
    with open(glossary_filepath, 'w') as _f:
        yaml.dump(data, _f, default_flow_style=False)


if __name__ == "__main__":
    include_drafts = os.getenv('include_drafts') or False
    execute(include_drafts)
