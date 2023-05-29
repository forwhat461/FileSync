import requests, os
from pathlib import Path
import hashlib


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()


target_url = ""


def init(_global_config):
    global global_config, target_url
    global_config = _global_config
    target_url = f"http://{global_config['target']}:{global_config['port']}"


global_config = {}


def check(fpath):
    with open(fpath, encoding='utf8') as f:
        file_content = f.read()
    _tmp = md5(file_content)
    resp_check = requests.post(
        target_url,
        json={"fpath": str(Path(fpath).relative_to(os.getcwd())), "content": [_tmp]},
        headers={"content-type": "application/json"},
    ).json()
    print(resp_check)  #
    if resp_check["state"]:
        if not resp_check["data"][0]:
            return
        resp_file = requests.post(
            target_url,
            json={
                "fpath": str(Path(fpath).relative_to(os.getcwd())),
                "replace": True,
                "content": file_content,
            },
            headers={"content-type": "application/json"},
        ).json()
    else:
        print("error")


def do(fpath):
    check(fpath)
