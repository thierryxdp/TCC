def filtraMultiplos(lista,n):
    """lista -> lista"""
    contador = 0
    juntar = ()
    listaF = []
    while contador < len(lista): 
        contador += 1
        if lista[contador]% n == 0:
            listaF = listaF + [lista[contador]]
    return listaF