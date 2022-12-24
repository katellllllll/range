from random import randint 

min, max = 0, 10

l = 10

arr1 = [randint(min, max) for i in range(l )]

arr2 = [arr1[i] for i in range(l ) if i % 2 == 0]

arr3 = [arr1[i] for i in range(l ) if i % 3 == 0]

arr4 = [arr1[i] for i in range(len(arr1) - 1, -1, -1)]

print("Arr1 = ", arr1)
print("Arr2 = ", arr2)
print("Arr3 = ", arr3)
print("Arr4 = ", arr4)
