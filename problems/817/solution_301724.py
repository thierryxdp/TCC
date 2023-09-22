def maiores (l, n):
    list.append (l, n)
    list.sort (l)
    return l[((list.index(l,n)) + 1): ]
def acima_da_media (l):
    if "1" in l:
        list.remove(l,1)
    if "2" in l:
        list.remove(l,2)
    if "3" in l:
        list.remove(l,3)
    if "4" in l:
        list.remove(l,4)
    return maiores (l)