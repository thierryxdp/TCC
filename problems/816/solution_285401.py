def insere(lista_num,n):
    lista_num.append(n)
    lista_num.sort()
    return lista_num

def maiores(numeros,numero):
    mIORES =insere(numeros,numero)
    del vasco[0:numero]
    return maiores