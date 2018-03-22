import pytest
from gpg_secrets import utils


class TestUtils(object):
    def setup_method(self):
        self.git_url = 'git@github.com:garyellis/ci-terraform.git'
        self.git_url_with_ref = 'git@github.com:garyellis/ci-terraform.git?ref=master'
        self.git_branch = 'master'
         
    def test_parse_git_url(self):
        config = utils.parse_git_url(self.git_url_with_ref)
        assert config['git_url'] == 'git@github.com:garyellis/ci-terraform.git'
        assert config['git_ref'] == 'master'

    def test_get_repo_invalid_url(self):
        repo = utils.get_repo('foo')
        assert repo is None

    def test_get_repo_default_branch(self):
        repo = utils.get_repo(self.git_url, self.git_branch)
        branch = repo.active_branch
        assert branch.name == 'master'
