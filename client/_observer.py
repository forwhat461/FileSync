import time, os
from watchdog.observers import Observer


def observe(EvHandler, global_config):
    observer = Observer()
    observer.schedule(EvHandler(), global_config["path"], recursive=True)

    print("observe", os.getcwd())
    observer.start()

    try:
        while True:
            time.sleep(1)
    except:
        observer.stop()

    observer.join()
