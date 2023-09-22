def filtraMultiplos(lista,n):
    """função que retorna os elementos da lista de entrada que são múltiplos do número n;
    Entrada: list(int||float), int||float 
    Saída: list(int||float)"""
    l = []
    i = 0
    
    while not i == len(lista):
        if lista[i] % n != 0:
            i = i + 1
        else:
            list.append(l,lista[i])
        	i = i + 1
    return l