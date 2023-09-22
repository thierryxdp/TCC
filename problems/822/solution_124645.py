def repetidos(lista):
    '''Função que retorna a quantidade de repetições de um número de entrada: list -> int'''
    indice = 1
    repetidos=[]
    while indice < len(lista):
        if lista[indice]==lista[indice-1]:
            repetidos.append(lista[indice])
        indice += 1 # indice = indice + 1
    return len(repetidos)