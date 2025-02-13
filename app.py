from http import HTTPStatus

from flask import Flask

from gh_parse.parse import find_readme_for_

app = Flask(__name__)


@app.route('/readme/<team>')
def fetch_readme_bor_team_view(team):
    try:
        readme = find_readme_for_(team)
    except LookupError:
        return {
            "error": "Team not found"
        }, HTTPStatus.NOT_FOUND
    return {
        "readme": readme
    }
