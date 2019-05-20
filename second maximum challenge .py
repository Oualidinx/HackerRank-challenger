#array = [10, 2, 3, 6, 5, 4, 8, 9, 1]
#array = [6, 5, 2, 4, 10, 3]
array = [1, 2, 8, 6, 41]

#second maximum challenge
def mth_smallest_value(array):
    index = 0
    for index in range(0,len(array)-1):
        i = index+1
        found = True
        while (found and i > 0):
            if array[i] < array[i-1]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
            else:
                found = False
            i -= 1
    #return array[m-1]
    return array

if __name__ == '__main__':
    print(mth_smallest_value(array))
    n = input()
    arr = input().split()
    arr = mth_smallest_value(arr)
    max = str(arr[len(arr) - 1])
    index = len(arr) - 1
    while (index >= 0):
        if arr[index] != max:
            max = arr[index]
            break
        index -= 1
    print(arr)
    print(max)
    print (int(arr))