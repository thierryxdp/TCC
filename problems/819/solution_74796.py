def multiplos(lista, n):
    'list, int ->list'
    i =0
    multiplos =[]
    
    while i<len(lista):
        if lista[i]%n ==0:
            multiplos =multiplos +[lista[i]]
        i =i+1
    return multiplos