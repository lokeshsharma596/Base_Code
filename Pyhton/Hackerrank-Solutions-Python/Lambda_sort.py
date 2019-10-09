arr = [(1, 2, 3), (3, 2, 1), (4, 2, 1), (6, 4, 3)]
indices = [(2, 0), (0, 1)]
# Solution------------------------


def indexSort(arr, indices):
    arr= [list(elem) for elem in arr]
    for i in range(0, len(indices)):
        for j in range(0, len(arr)-1):
            if indices[i][1] == 0:
                if arr[j][indices[i][0]] > arr[j+1][indices[i][0]]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

            elif indices[i][1] == 1:
                if arr[j][indices[i][0]] < arr[j+1][indices[i][0]]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    
    
    # it prints list of lists
    print(arr)

    arr = [tuple(elem) for elem in arr]

    # it prints list of tuples
    print(arr)


indexSort(arr, indices)


