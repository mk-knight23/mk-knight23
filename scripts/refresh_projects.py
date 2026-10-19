"""Refresh public project evidence. Standard library only; no third-party card API."""
import argparse
import datetime as dt
import html
import json
import os
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['MK-QuizFlow', 'AI-ASSISTANTS-ECOSYSTEM', 'AI-ASSISTANT-OPENCODE',
         'AI-SDK-ANTHROPIC', 'mkazi-time-router']
START, END = '<!-- PROJECT-SNAPSHOT:START -->', '<!-- PROJECT-SNAPSHOT:END -->'


def collect():
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'mk-profile-evidence'}
    if os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    projects = []
    for name in NAMES:
        req = urllib.request.Request('https://api.github.com/repos/mk-knight23/' + name, headers=headers)
        with urllib.request.urlopen(req, timeout=25) as response:
            data = json.load(response)
        if data.get('private') or data['full_name'].lower() != ('mk-knight23/' + name).lower():
            raise ValueError('Expected the configured public repository')
        projects.append({key: data.get(key) for key in ['name', 'full_name', 'language',
                        'stargazers_count', 'forks_count', 'pushed_at', 'html_url', 'private']})
    return projects


def render(projects, checked_at):
    if len(projects) != len(NAMES) or {p['name'] for p in projects} != set(NAMES):
        raise ValueError('Incomplete project snapshot; retaining previous files')
    lines = [START, f'Public repository snapshot · checked {checked_at[:10]} UTC.', '',
             '| Repository | Main language | Stars | Last pushed (UTC) |',
             '| --- | --- | ---: | --- |']
    for p in projects:
        if p.get('private') or not re.fullmatch(r'[A-Za-z0-9_.-]+', p['name']):
            raise ValueError('Invalid public repository metadata')
        stars = p['stargazers_count']
        if not isinstance(stars, int) or stars < 0:
            raise ValueError('Invalid star count')
        # Construct links from the allowlisted owner instead of API-provided URLs.
        lines.append(f"| [{p['name']}](https://github.com/mk-knight23/{p['name']}) | {p['language'] or '—'} | {stars} | {p['pushed_at'][:10]} |")
    lines += ['', 'Repository metadata is a dated snapshot, not a measure of engineering quality, employment or client adoption.', END]
    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text()
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(END) < readme.index(START):
        raise ValueError('Expected exactly one ordered pair of README markers')
    readme = readme[:readme.index(START)] + '\n'.join(lines) + readme[readme.index(END) + len(END):]
    # Finish validation before changing any existing evidence.
    snapshot = json.dumps({'checked_at': checked_at, 'scope': 'five selected public repositories',
                           'projects': projects}, indent=2) + '\n'
    (ROOT / 'data').mkdir(exist_ok=True)
    (ROOT / 'data/projects.json').write_text(snapshot)
    readme_path.write_text(readme)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fixture', type=Path, help='Render previously retrieved metadata offline')
    args = parser.parse_args()
    projects = json.loads(args.fixture.read_text()) if args.fixture else collect()
    render(projects, dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'))
