import os, json, sys
import _observer
import _fileFilter
import _debounce
import _requests

global_config = {}

class EvHandler:
    @_debounce.Debounce(0.5)
    def dispatch(self, ev):
        if _fileFilter.filterFunc(ev):
            _requests.do(ev.src_path)


def main():
    global global_config
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(f"{path}/fsync.conf") as fp:
            global_config = json.load(fp)
        os.chdir(sys.argv[1])
        global_config["path"] = sys.argv[1]
        _requests.init(global_config)
        print(global_config)
    else:
        print("~ <file_path> /fsync.conf")
        quit()

    _observer.observe(EvHandler, global_config)

if(__name__ == '__main__'):
    main()
