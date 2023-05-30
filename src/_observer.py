import time, os
from watchdog.observers import Observer

global_config = {}
observer = {}
def init(_global_config):
    global global_config
    global_config = _global_config

def observe(EvHandler):
    global global_config, observer
    observer = Observer()
    observer.schedule(EvHandler(), global_config["path"], recursive=True)

    print("observe", os.getcwd())
    observer.start()

def stop():
    global observer
    observer.stop()
    observer.join()

