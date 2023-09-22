def repetidos(x):
    contador = 0
    for num in range(0 , x+1):
        if num in x:
            contador = contador + 1
    return contador