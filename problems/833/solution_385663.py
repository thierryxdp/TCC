conta_numero(numero, matriz):
    counter = 0
    for lista in Matriz:
        
        for elem in lista:
            if elem == numero:
                counter +=1
    return counter