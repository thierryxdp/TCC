def repetidos(lista):
    contador=1
    num_repetidos=0
    while contador<len(lista):
        if lista[contador] == lista[(contador)-1]:
            num_repetidos+=1
        contador+=1
    return num_repetidos