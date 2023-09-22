def total(lista,produtos):
    res=[]
    for i in range(0,len(lista)) :
        if lista[i] in produtos:
            c=produtos[lista[i]]
            list.append(res,c)
    return sum(res)