import git
import yaml
import logging
import os
import re
import shutil

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def resolve_git_repo(url):
    """
    """
    config = parse_git_url(url)
    repo = get_repo(config['git_url'], config['git_ref'])
    repo.working_dir

def get_repo(url, clean=True, branch='master'):
    """
    Clones and returns a Git.Repo
    """
    if '.git' not in url:
        return

    to_dir = os.path.basename(url).split('.')[0]

    if clean:
        try:
            shutil.rmtree(to_dir,ignore_errors=True)
        except shutil.Error as err:
            log.error(err.message)

    log.info('cloning repo: {} to: {}'.format(url, to_dir))
    repo = git.Repo.clone_from(url, to_dir, branch=branch)
    return repo

def parse_git_url(url):
    """
    Extract the git repo and ref from the input url
    """
    config = {
        'type': 'git',
        'git_url': None,
        'git_ref': None
    }

    match_git_url =  re.search('(.*git)', url)
    match_git_url_ref = re.search('(?<=[?]ref=).*', url)

    if match_git_url:
        config['git_url'] = match_git_url.group(0)

    if match_git_url_ref:
        config['git_ref'] = match_git_url_ref.group(0)

    return config

def gen_source_gpg_env_str(paths):
    """
    Render a string of gpg decrypt commands
    """
    source_gpg_env_tpl = 'source <$(gpg -d no-tty {})'
    for i, gpg_file in enumerate(paths):
        source_gpg_env_str += source_gpg_env_tpl.format(gpg_file)
        if i <  len(paths):
            source_gpg_env_str += ' &&'
