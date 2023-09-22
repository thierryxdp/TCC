def filtra_pares(a,b,c,d):
    '''retorna uma nova tupla contendo apenas os elementos pares da dupla dada, dados numeros inteiros'''
    lista1 = [a,b,c,d]
    lista2 = []
    for valor in lista1:
        if valor % 2 == 0:
            lista2.append(valor)
            return (lista2)