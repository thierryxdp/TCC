def total(lista,dic):
    i=0
    for lista in dic:
        i=i+1
        if lista in dic:
            p=list(lista[i])
            dic=sum(tuple(dic[p]))
             
    return dic