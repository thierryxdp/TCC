def filtra_pares(tupla,n):
    """retorna os números pares dentro da tupla inserida
    tuple -> tuple"""
    
    lista=list(tupla)
    lista_pronta=[i for i in lista if i%n==0]
    
    return tuple(lista_pronta)