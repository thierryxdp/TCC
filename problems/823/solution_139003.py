def faltante(l):
    l = list.sort(l)
   
    ls = list(range(1))
    for i in ls:
        if i not in l:
            return l
    return l