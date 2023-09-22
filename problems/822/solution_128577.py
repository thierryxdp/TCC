def repetidos(lista):
    x = 0
    rep = 0
    
    while x < len(lista) - 1:
        if lista[x] == lista[x +1]:
        	rep += 1
        x += 1
    
    return rep