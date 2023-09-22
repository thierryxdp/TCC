def posLetra (f,l,n):
    o=str.count(f,l)
    f2=str.replace(f,l,'.',(n-1))
    if o<n:
        return -1
    else:
        return str.find(f2,l)