def posLetra(string, letra, n):
    count = 0
    for e, el in enumerate(string):
        if el == letra:
            count += 1
            
        if count == n:
            break
            
    if count != n:
        return -1
        
    return count