array = list({8, 7, 6, 5, 4, 3, 1, 4})
for i in range(1, len(array)):
    key = array[i]
    j = i-1
    while j >= 0 and key < array[j]:
        array[j], array[j+1] = array[j+1], array[j]
        j -= 1
    array[j+1] = key

print(array)
