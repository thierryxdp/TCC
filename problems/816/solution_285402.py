def insere(lista_num,n):
    lista_num.append(n)
    lista_num.sort()
    return lista_num

def maiores(numeros,numero):
    maiores =insere(numeros,numero)
    del maioes [0:numero]
    return maiores