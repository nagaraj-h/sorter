def sort(a, ascending=True):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if (a[j] > a[j+1] and ascending) or (a[j] < a[j+1] and not ascending):
                a[j], a[j+1] = a[j+1], a[j]

    return a

def sort_test():
    arr1 = [2,3,7,896,88,65,45, 787,565]
    arr1_sorted_asc = [2,3,7,45,65,88,565,787,896]

    arr2 = [394, 951, 518, 292, 311, 239, 22, 917, 921, 478, 478, 478, 441]
    arr2_sorted_desc = [951, 921, 917, 518, 478, 478, 478, 441, 394, 311, 292, 239, 22]


    if sort(arr1, True) == arr1_sorted_asc and sort(arr2, False) == arr2_sorted_desc:
        print('Sorting Algorithm Works')
    else:
        print('Sorting Algorithm Has Bugs')

sort_test()
