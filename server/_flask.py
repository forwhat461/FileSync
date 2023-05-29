
from flask import Flask, request
from pathlib import Path
import os,json
import hashlib

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

app = Flask("file sync server")

global_config = {}

def init(_global_config):
    global global_config
    global_config = _global_config

@app.route("/", methods=["POST", "GET"])
def api():
    global global_config
    form_data = request.get_json()
    needReplace = 0
    if not form_data.get("fpath"): return
    fpath = Path(f"{global_config['path']}/{form_data['fpath']}")
    if(form_data.get('replace')):
        if(not fpath.parent.is_dir()):
            os.makedirs(str(fpath.parent))
        fp = open(str(fpath), 'w')
        fp.write(form_data['content'])
        
        print('replaced', str(fpath))
        return json.dumps({"state": True})
    else:
        if fpath.is_file():
            with open(str(fpath)) as fp:
                file_content = fp.read()
        else:
            file_content = ""
        if form_data["content"][0] != md5(file_content):
            needReplace = 1
    return json.dumps({"state": True, "data": [needReplace]})

def main():
    app.run(debug=True, host="0.0.0.0", port=global_config["port"])