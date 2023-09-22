def posLetra(s,l,n):
    u=str.count(s,l)
    f=str.replace(s,l,'.',(n-1))
    if u<n:
        return -1
    else:
        return str.find(f,l)