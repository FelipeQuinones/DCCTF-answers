from hashlib import md5
string = "aviciaban"
string_to_hash = string.encode()
answer = md5(string_to_hash).hexdigest()
print(answer)