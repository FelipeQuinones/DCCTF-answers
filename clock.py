from hashlib import md5

for h in range(0,25):
    for m in range(0,61):
        for s in range(0, 61):
            resst = f"{h}:{m}:{s}"
            res = md5(resst.encode())
            if res.hexdigest() == "5bc3223650036e1efe6733b585746bf8":
                print(resst)
