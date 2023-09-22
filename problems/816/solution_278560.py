def maiores(lista,n):
    maior=[]
    for item in lista:
        if item >n:
            maior.append(item)
    ordem = list.sort(maior)
    return ordem