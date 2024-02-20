
from flask import Flask, render_template, redirect, url_for, request, jsonify, Response, flash, send_file
from flask.templating import TemplateNotFound

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')


@app.route("/")
def index():
    return redirect(url_for('dashboard'))


if __name__ == "__main__":
    app.run(port=29111)
