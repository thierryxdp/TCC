def colchao(lista,H,L):
    """ dada as dimensoes de um colchao vamos determinar se ele passa pela porta
        entrada --> int
        saida   --> int"""
    A = lista[0]
    B = lista[1]
    C = lista[2]
    if (H >= B and L >=A):
        return True
    elif (L >= B and H >=A):
        return True
    else:
        return False
    """ teste
    resultados esperados:
    Entrada: [25,120,220], 200, 100 ; Saida: True
    Entrada: [25,205,220], 200, 100 ; Saida: False
    Entrada: [25,200,220], 200, 100 ; Saida: True
    
    resultados obtidos:
    >>> colchao([25,200,220],200,100)
    True
    >>> colchao([25,205,220],200,100)
    False
    >>> colchao([25,120,220],200,100)
    True"""