def conta_numero(numero, matriz):
    "Retorna quantas vezes o nuúmero aparece na matriz. int,list->int"
    cont = 0
    for linha in matriz:
        for numero in linha:
        	cont += 1    
    return cont