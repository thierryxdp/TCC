def inverte(a):
    a=str.replace(a,","," ")
    a=str.lower(a)
    a=str.split(a)
    a=a[100::-1]
    a=str.join(" ",a)

    return a