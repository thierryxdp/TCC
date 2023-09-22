def maiores(ls, n):
    list.sort(ls)
    if n in ls:
        a = ls.index(n)
        b = ls.index(n)
        return ls[a+b+1]
    else:
        ls.append(n)
        list.sort(ls)
        c = ls.index(n)
        if ls[c] == max(ls):
            return []
        if ls[c] == min(ls):
            return ls[1:]
        else:
            return ls[c+1:]