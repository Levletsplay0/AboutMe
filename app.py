from flask import Flask, render_template
import requests
import json

token = "token GITHUB_TOKEN" #https://github.com/settings/tokens

def get_github_repos():
    try:
        headers = {"Authorization": token}
        response = requests.get("https://api.github.com/user/repos", headers=headers)
        repos = response.json()
        
        repo_data = [[repo["name"], repo["language"], "Да" if repo["private"] else "Нет"] for repo in repos]
        return repo_data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к GitHub API: {e}")
        return []
    


def get_github_user_profile():
    try:
        headers = {"Authorization": token}
        response = requests.get("https://api.github.com/users/Levletsplay0", headers=headers)
        avatar_url = response.json()["avatar_url"]
        name = response.json()["name"]
        url = response.json()["html_url"]
        return avatar_url, name, url
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к GitHub API: {e}")
        return []
    

app = Flask(__name__)



@app.route("/")
def index():
    avatar_url, name, url = get_github_user_profile()
    repo_data= get_github_repos()
    return render_template("index.html", repo_data=repo_data, name=name, avatar_url=avatar_url, url=url)


app.run(debug=True, host="0.0.0.0")