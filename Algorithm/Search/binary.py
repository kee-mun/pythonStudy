def search(target, someList):
    start_index, end_index = 0, len(someList)-1

    while start_index <= end_index:
        i = (start_index + end_index) // 2
        if someList[i] == target:
            return i
        elif someList[i] > target:
            end_index = i - 1
        else:
            start_index = i + 1
    return None

print(search(2,[2,3,5,7,11]))
print(search(0,[2,3,5,7,11]))
print(search(5,[2,3,5,7,11]))
print(search(3,[2,3,5,7,11]))
print(search(11,[2,3,5,7,11]))
