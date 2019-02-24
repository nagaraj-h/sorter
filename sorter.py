def sort(a, ascending=True):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    if ascending:
        return a
    else:
        return a[::-1]

