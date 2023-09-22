def conta_numero(numero, matriz):
    "Retorna quantas vezes o nuúmero aparece na matriz. int,list->int"
    cont1 = 0
    
    for numero in matriz:
        cont = list.count(matriz, numero)
        cont1+=cont
    return cont1