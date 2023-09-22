def filtra_pares (n1, n2, n3, n4):
    '''Função que fitra os elementos pares dados 4 números
    int, int, int, int -> tupla'''
    tupla1 = (n1, n2, n3, n4)
    tupla2 = ()
    for valor in tupla1:
        if valor % 2 == 0:
            tupla2.append(valor)