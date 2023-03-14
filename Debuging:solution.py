def quick_sort(numbers):
# corrected the indentantion of block of code
    quick_sort_helper(numbers, 0, len(numbers)-1)
# Corrected the indentation of this block of code
def quick_sort_helper(numbers, first, last):
    if first<last:
        splitpoint = partition(numbers, first, last)
        quick_sort_helper(numbers, first, splitpoint-1)
        quick_sort_helper(numbers, splitpoint+1, last)


def partition(numbers, first, last):
    pivotvalue = numbers[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
# corrected the conditions of the while loop
# the were causing an  index out of range error
# correct the indentation of the block of code
       while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while numbers[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark: # remove the -1
           done = True
       else:
           temp = numbers[leftmark]
           numbers[leftmark] = numbers[rightmark]
           numbers[rightmark] = temp

    temp = numbers[first]
    numbers[first] = numbers[rightmark]
    numbers[rightmark] = temp

    return rightmark

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))
