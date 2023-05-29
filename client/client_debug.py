import client, sys
from werkzeug._reloader import run_with_reloader

sys.argv = ['F:/PY/样例/扩展/文本/FileSync/client/client_debug.py', 'F:/PY']
run_with_reloader(client.main) 
