def bubble_sort(list_numbers):
    n = len(list_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_numbers[j] > list_numbers[j + 1]:
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]


numbers = [64, 34, 25, 12, 22, 11, 128]
print("Original list:", numbers)

bubble_sort(numbers)
print("Sorted list:", numbers)


#this is the test function
def foo(): 
    pass
