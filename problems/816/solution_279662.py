def maiores(lista, n):
    tamanho=len(lista)
    i=0
    lista2=[]
    while i <= tamanho:
        if lista[i]>n:
            lista2.append(lista[i])
        i=i+1
    return lista2