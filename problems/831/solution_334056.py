def lingua_p(a):
    b=''
    for i in range(len(a)):
        if (a[i] in 'aeiouAEIOU'):
            b=b+a[i]+'p'
        else:
            b=b+a[i]
    return b