import os, json, sys, time
import _observer
import _fileFilter
import _debounce
import _requests
import _flask

global_config = {}


class EvHandler:
    @_debounce.Debounce(0.1)
    def dispatch(self, ev):
        if _fileFilter.filterFunc(ev):
            print(ev)
            _requests.do(ev.src_path)


def main():
    global global_config
    if len(sys.argv) == 1:
        print("~ <file_path> /fsync.conf")
        exit()
    with open(f"{sys.argv[1]}/fsync.conf") as fp:
        global_config = json.load(fp)
    os.chdir(sys.argv[1])
    global_config["path"] = sys.argv[1]

    _requests.init(global_config)
    _flask.init(global_config)
    _observer.init(global_config)
    print(global_config)
    _observer.observe(EvHandler)
    _flask.main()

    _observer.stop()
    exit()


if __name__ == "__main__":
    main()
