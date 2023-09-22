def filtraMultiplos (lista,n):
    "Funçao que retorna todos os elementos de uma lista que são divisívei por um número n"
    multiplos = []
    i=0
    while i<len(lista):
        if lista[i]% n ==0:
            multiplos = multiplos + [lista[i]]
        i = i+1
    return multiplos