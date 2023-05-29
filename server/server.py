import sys, json, os
import _flask

if len(sys.argv) > 1:
    path = sys.argv[1]
    with open(f"{path}/fsync.server.conf") as fp:
        global_config = json.load(fp)
    global_config["path"] = sys.argv[1]
    _flask.init(global_config)
    print(global_config)
    _flask.main()
else:
    print("~ <file_path> /fsync.server.conf")
    quit()
