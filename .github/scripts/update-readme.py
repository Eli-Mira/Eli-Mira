#!/usr/bin/env python3
"""Update the project highlights section in the profile README."""

import os
import re
import json
import urllib.request

def main():
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print('No GITHUB_TOKEN provided')
        return

    url = 'https://api.github.com/user/repos?per_page=100&sort=updated'
    req = urllib.request.Request(url, headers={
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    })
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read())

    main_projects = ['gesture-control', 'dev-squad', 'fruit-slicer']
    project_lines = []
    for repo in repos:
        if repo['name'] in main_projects:
            desc = repo.get('description') or 'No description'
            project_lines.append(f'- **[{repo['name']}](https://github.com/Eli-Mira/{repo['name']})**: {desc}')

    if not project_lines:
        print('No main projects found')
        return

    with open('README.md', 'r') as f:
        content = f.read()

    pattern = r'(## Building\n\n)(.*?)(\n## )'
    replacement = f'\\1{'\\n'.join(project_lines)}\\3'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    if new_content == content:
        print('No changes needed')
        return

    with open('README.md', 'w') as f:
        f.write(new_content)

    print(f'Updated {len(project_lines)} projects in README')

if __name__ == '__main__':
    main()
