def filtra_pares(tupla):
    '''funcao que filtra uma yupla retornando apenas
os valores pares; tup(int,int,int,int) -> tup''' 
    n = list(tupla)
    lista1 = n
    lista2 = []
    for valor in lista1:
        if valor%2 == 0:
            lista2.append(valor)
    return tuple(lista2)