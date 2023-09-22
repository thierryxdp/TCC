def filtra_pares(tupla):
    """retorna os números pares dentro da tupla inserida
    tuple -> tuple"""
    
    lista=list(tupla)
    lista_pronta=[i for i in lista if i%2==0]
    
    return tuple(lista_pronta)