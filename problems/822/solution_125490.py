def repetidos(lista):
    contador=0
    vezes = 0
    for numero in lista:
        if contador == len(lista)-1:
            break
        if numero == lista[contador+1]:
            vezes+=1
        contador+=1
    return vezes