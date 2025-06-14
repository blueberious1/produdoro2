from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.after_request
def add_permissions_policy(response):
    response.headers["Permissions-Policy"] = "autoplay=(self)"
    return response

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/todolist')
def todolist():
    return render_template("todolist.html")

if __name__ == '__main__':
    app.run(debug=True)

