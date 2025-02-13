from functools import cache

from github import Github

from gh_parse.config import GITHUB_TOKEN, GITHUB_REPO_NAME

github = Github(GITHUB_TOKEN)
repo = github.get_user().get_repo(GITHUB_REPO_NAME)


def get_readme_contents(branch):
    return repo.get_contents(
        "README.md",
        ref=branch.name
    ).decoded_content.decode("utf8").casefold()


def valid_branch(branch, team):
    readme = get_readme_contents(branch)
    return team in readme


@cache
def find_team_branch(team):
    for branch in repo.get_branches():
        if valid_branch(branch, team):
            return branch
    raise LookupError(f"Team `{team}` not found")


def find_readme_for_(team):
    team = team.casefold()
    team_branch = find_team_branch(team)
    readme = get_readme_contents(team_branch)
    if not readme:
        raise LookupError(f"Team `{team}` not found")
    return readme
