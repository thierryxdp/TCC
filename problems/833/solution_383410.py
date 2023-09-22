def conta_numero(numero, matriz):
    "Retorna quantas vezes o nuúmero aparece na matriz. int,list->int"
    #cont = 0
    num = numero
    for numero in matriz:
        cont = 0
        if num == numero:
            cont += 1
    return cont