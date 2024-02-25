import re

def extract_about_text(text: str) -> str:
    ''' Extract text in ### About section of md file '''

    text = text.replace('\n', '')
    pattern = re.compile(r'###\sAbout(.*?)\s*###', re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) >= 1:
        return matches[0].strip()
    else:
        return None