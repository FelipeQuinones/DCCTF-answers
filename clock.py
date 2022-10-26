from hashlib import md5
from time import time

for h in range(0,25):
    for m in range(0,61):
        for s in range(0, 61):
            time_ = f"{h}:{m}:{s}"
            time_to_hash = md5(time_.encode())
            if time_to_hash.hexdigest() == "5bc3223650036e1efe6733b585746bf8":
                print(time_)
