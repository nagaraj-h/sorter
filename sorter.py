def sort(a, ascending=True):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    if ascending:
        return a
    else:
        return a[::-1]
