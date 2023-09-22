def filtraMultiplos(lista,n):
    """Filtra os múltiplos de um número n
    	list, int -> list
        Parameters:
        lista: Lista de números
        n: Número a partir do qual serão definidos os múltiplos
        
        Returns:
        Os múltiplos de n dentro da lista
    """
    i = 0
    divisiveis = []
    
    while i < len(lista):
        if lista[i]%numero == 0:
            divisiveis.append(lista[i])
        i = i+1
        
    return divisiveis