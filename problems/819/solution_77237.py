def filtraMultiplos(lista,n):
    """Filtra os múltiplos de um número n"""
    
    mult = []
    i = 0
    
    if lista[i]%n == 0:
        mult.append(lista)
        listmult = filter(mult,lista)
    i=+1
        
    return listmult