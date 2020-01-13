import hashlib

str1 = "naver"
str2 = "Hello World!"

result = hashlib.sha256(str1.encode())

print(str1, "sha256")
print(result.hexdigest())

result = hashlib.sha256(str2.encode())
print(str2,"sha256")
print(result.hexdigest())