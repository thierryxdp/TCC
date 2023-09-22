def inverte(a):
    a=str.lower(a)
    a=str.split(a)
    a=a[100::-1]
    a=str.join(" ",a)
    a=str.strip(a,";")
    a=str.strip(a,"?")
    a=str.strip(a,"-")
    a=str.strip(a,",")
    return a