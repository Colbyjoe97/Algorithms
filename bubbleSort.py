def sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # 1 line method
                # arr[j], arr[j+1] = arr[j+1], arr[j]
    print arr

sort([1,3,2,6,4,5])