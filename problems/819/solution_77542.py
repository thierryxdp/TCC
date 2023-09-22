def filtraMultiplos (lista, n):
    multiplos = list()
    i = 0
    resposta =list()
    while (i<len(lista)):
        if (lista[i]% n == 0):
            multiplos +=(lista[i],)
                 
        i += 1
        
    return multiplos