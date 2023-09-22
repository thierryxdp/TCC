def total(ls, d):
    sol=[]
    for i in ls:
        if i in d:
            sol.append(d[i])
        return round(sum(sol),2)