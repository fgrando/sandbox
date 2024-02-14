#!/bin/python3

import os
import sys
import time
import signal
import threading


# keep running this thread if the list has at least one item
KEEP_ALIVE = threading.Lock()

def process(path):
    if path.endswith('.txt'):
        with open(path) as fd:
            print(fd.read())
        os.remove(path)

def handler(signum, frame):
    print(f"\nCtrl-c detected. Stopping threads...({signum})")
    KEEP_ALIVE.release()





class FileMonitor(threading.Thread):
    def __init__(self, folder, keep_alive_lock, process_func, wait_seconds=0):
        super(FileMonitor, self).__init__()
        self.daemon = False  # If True, allow main to exit even if still running.
        self.paused = True  # Start out paused.
        self.state = threading.Condition()
        self.folder = folder
        self.process = process_func
        self.sleep_s = wait_seconds
        self.keep_alive = keep_alive_lock

    def run(self):
        while self.keep_alive.locked():
            # process all found files
            for f in os.listdir(folder):
                full_path = os.path.join(folder, f)
                self.process(full_path)

            # wait time
            for i in range(self.sleep_s):
                time.sleep(1)
                if not self.keep_alive.locked():
                    # abort wait time if keep alive is false
                    break
            print('.')
        print("monitor stopped")



def run(folder):
    KEEP_ALIVE.acquire()
    wait_seconds = 3
    mon = FileMonitor(os.path.abspath(folder), KEEP_ALIVE, process, wait_seconds)
    mon.start()
    mon.join()

    print("bye!")
    return 0


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)

    folder = sys.argv[1]
    print(f"monitoring folder {folder}")
    exit(run(folder))