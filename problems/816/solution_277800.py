def maiores(listan,n):
    listan.insert(0,n)
    list.sort(listan)
    a=listan.index(n)
    return listan[a+1:]