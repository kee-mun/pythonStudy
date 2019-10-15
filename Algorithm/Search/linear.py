def search(target, someList):
    for i in range(0,len(someList)):
        if someList[i] == target:
            return i
    return None

print(search(2,[2,3,5,7,11]))
print(search(0,[2,3,5,7,11]))
print(search(5,[2,3,5,7,11]))
print(search(3,[2,3,5,7,11]))
print(search(11,[2,3,5,7,11]))
