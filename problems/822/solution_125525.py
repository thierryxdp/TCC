def repetidos(lista):
    lst = []
    i=1
    while i<len(lista):
        if lista[i-1] == lista[i]:
            list.append(lst,1)
        i=i+1
    return sum(lst)