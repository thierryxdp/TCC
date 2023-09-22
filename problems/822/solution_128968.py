def repetidos(lista=[]):
    valor = 0
    for i in range(len(lista)):
        if i > 0 and lista[i]==lista[i-1]:
            valor+=1
    return valor