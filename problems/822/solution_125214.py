def repetidos(lista):
    
    i=0
    contador = 0
    while i < len(lista):
        if lista[i] == 0:
            contador = contador
        elif lista[i] == lista[i-1]:
            contador = contador + 1
  
        i = i+1
    return contador