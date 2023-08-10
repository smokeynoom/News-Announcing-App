from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
data_file = os.path.join("data", "announcements.json")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        save_announcement(title, content)
        return redirect(url_for("index"))
    return render_template("index.html", announcements=get_announcements())

def save_announcement(title, content):
    content = content.replace("\n", "<br>")
    announcements = get_announcements()
    announcements.append({"title": title, "content": content})
    with open(data_file, "w") as f:
        json.dump(announcements, f, indent=2)

def get_announcements():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    app.run(debug=True)
