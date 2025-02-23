import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.running = False

    def start(self):
        self.start_time = time.time()
        self.running = True

    def stop(self):
        self.running = False

    def get_elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        return 0
