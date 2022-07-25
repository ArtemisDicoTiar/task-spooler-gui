import json
import subprocess
from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/hello")
def hello_world():
    return "Hello, World!"

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/tsp/list")
def list():
    output = subprocess.check_output("tsp -l", shell=True, encoding="utf-8")
    print(output)
    lines = output.splitlines()
    header_line = lines[0]
    column_names = header_line.split(maxsplit=5)
    print(column_names)
    assert column_names[-1] == "Command [run=0/1]", column_names[-1]
    lines = lines[1:]
    lines = [l.split(maxsplit=5) for l in lines]
    lines_by_header = [dict(zip(column_names, column_datas)) for column_datas in lines]
    print(json.dumps(lines_by_header, indent=2))
    return jsonify(lines_by_header)

def test_list():
    list()
