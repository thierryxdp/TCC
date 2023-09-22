def conta_numero(numero, matriz):
    "Retorna quantas vezes o nuúmero aparece na matriz. int,list->int"
    #cont = 0
    
    for numero in matriz:
        cont = list.count(matriz, numero)
        #cont += 1
    return cont