def maiores(lista,n):
    #retorna os valores na lista maiores que n.
    #list,int - list
    listanova=[]
    for i in range(len(lista)):
        if lista[i] > n:
            listanova.append(lista[i])
        else:
            continue
    return listanova