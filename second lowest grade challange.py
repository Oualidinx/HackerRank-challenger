#second lowest grade challange
def mth_smallest_value(array):
    index = 0
    for index in range(0,len(array)-1):
        i = index+1
        found = True
        while (found and i > 0):
            if array[i][1] < array[i-1][1]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
            else:
                found = False
            i -= 1
    #return array[m-1]
    return array

def second_element(val):
    return val[0]

def print_highest_score(array):
    start = 0
    end = len(array)-1
    while(True):
        if array[start][1] == array[start+1][1]:
            start+=1
        else:
            break
    start = start + 1

    while(True):
        if array[end][1] == array[start][1]:
            break
        end -= 1
    res = array[start:end+1]
    res.sort(key = second_element)
    res = [res[i][0] for i in range(0 , len(res))]
    return res


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students = mth_smallest_value(students)
    final_students = print_highest_score(students)
    for name in final_students:
        print(name)