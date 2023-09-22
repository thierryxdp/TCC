def posLetra(string, letra, n):
    count = 0
    index = -1
    for e, el in enumerate(string):
        if el == letra:
            count += 1
            
        if count == n:
            index = e
            break
            
        
    return index