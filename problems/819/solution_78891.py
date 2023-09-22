def filtraMultiplos(lista,n):
    """Filtra os múltimos do número n dado como entrada;
    list, int-> list"""
    i=0
    lista_filtrada= []
    
    while i < len(lista):
        if lista[i] % n ==0:
            lista_filtrada += lista[i]
        i +=1
    return lista_filtrada