def filtraMultiplos (lista, numero):
    """Função que filtra os multiplos de um numero n dentro de uma lista,
    Entrada: lista[float], float.
    Saída: lista[float]"""
    
    i = 0
    multiplos = []
    
    while i < len(lista):
    	if lista[i]%numero == 0:
            list.append(multiplos, lista[i])
        i = i+1
    return multiplos