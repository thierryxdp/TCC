def filtraMultiplos (lista, numero):
    """Função que filtra os multiplos de um numero n dentro de uma lista,
    Entrada: lista[float], float.
    Saída: lista[float]"""
    
    i = 0
    multiplos = ''
    
    while lista[i]%2 == 0:
    	i = i+1
        multiplos = multiplos + lista[i]
    return multiplos