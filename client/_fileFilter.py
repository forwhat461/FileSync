from pathlib import Path


def filterFunc(ev):
    f = Path(ev.src_path)
    if [".py", ".txt", ".conf", ".md"].count(f.suffix):
        return True
    return False
