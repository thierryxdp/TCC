def filtraMultiplos (lista, n):
    multiplos = list()
    i = 0
    resposta =list()
    while (i<len(lista)):
        if (n % lista[i] == 0):
            multiplos += (lista[i],)
                 
        i += 1
        
    return multiplos