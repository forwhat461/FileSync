import threading

class Debounce:
    def __init__(self, interval):
        self.interval = interval
        self.debounced = None

    def __call__(self, func):
        def decorator(*args, **kwargs):
            if self.debounced is not None:
                self.debounced.cancel()
            self.debounced = threading.Timer(self.interval, func, args, kwargs)
            self.debounced.start()
        return decorator