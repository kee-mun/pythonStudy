#Quick Sorting Algorithm에 대해서
#퀵소트알고리즘은 Unsorted List에서 임의의 Pivot값을 정해
#Pivot 값보다 작은 값은 PIvot의 왼쪽으로
#Pivot 값보다 큰 값은 Pivot의 오른쪽으로 보내서 데이터 정렬하는 방식

# Quick Sorting Algorithm의 O()는
# 최선 O(n Log(n)) 최악 O(n^2) 평균 O(n log(n))의 복잡도를 가진다.

def quicksorted(arr):
    if len(arr) > 1:
        pivot = arr[(len(arr)-1)//2]
        left, mid, right = [],[],[]
        for i in range(len(arr)):
            if arr[i] > pivot:
                right.append(arr[i])
            elif arr[i] < pivot:
                left.append(arr[i])
            else:
                mid.append(arr[i])
        return quicksorted(left) + mid + quicksorted(right)
    else:
        return arr


unsortedList = [1,2,5,4,3,8,7,5]
sortedList = [1,2,3,4,5,5,7,8]

if quicksorted(unsortedList) == sortedList:
    print("정답!")
else:
    print("오답!")