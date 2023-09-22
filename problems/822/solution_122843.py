def repetidos(cont):
    lista = [1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]
    cont = 0
    for i in range(len(lista)):
        if lista[i] == (5):
            cont += 1
    return cont