def repetidos (lista):
    lista2=''
    c = 0
    c1= 1
    for c in lista:
        if lista[c] == lista[c1]:
            lista2=lista2+1
        c=c+1
        c1=c1+1
    return lista2