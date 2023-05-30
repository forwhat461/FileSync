import requests, os
from pathlib import Path
import hashlib


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


target_url = ""


def init(_global_config):
    global global_config, target_url
    global_config = _global_config
    target_url = f"http://{global_config['target']}:{global_config['target_port']}"


def post(json):
    try:
        resp = requests.post(
            target_url, json=json, headers={"content-type": "application/json"}
        )
        resp.raise_for_status()
        return resp.json()
    except:
        return False


global_config = {}



def check(fpath, file_content):
    _tmp = md5(file_content)
    resp_check = post(
        {"fpath": str(Path(fpath).relative_to(os.getcwd())), "content": [_tmp]}
    )
    if not resp_check:
        return print("连不上")
    print(resp_check)  #
    if resp_check["state"]:
        if resp_check["data"][0]:
            return True
        return False
    else:
        return print("error")

def replace(fpath, file_content):
    resp_file = post(
        {
            "fpath": str(Path(fpath).relative_to(os.getcwd())),
            "replace": True,
            "content": file_content,
        }
    )
    if not resp_file:
        return print("网不好?")
    print(resp_file)

def do(fpath):
    file_content = ''
    with open(fpath, encoding="utf8") as f:
        file_content = f.read()
    if(check(fpath, file_content)):
        replace(fpath, file_content)

