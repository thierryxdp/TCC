def filtraMultiplos(lista,n):
    """lista -> lista"""
    contador = 0
    juntar = ()
    listaF = []
    while contador < len(lista):
        
        if lista[contador]% n == 0:
            listaF = listaF + lista[contador]
        contador += 1
    return listaF