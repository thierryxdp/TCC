def posLetra(s,l,n):
    i=0
    r=0
    while i<n:
    r=r + str.index(s, l, n)
    s=s[r:]
    i=i+1
    return r