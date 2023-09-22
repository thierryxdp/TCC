def repetidos(lista):
    ''' funcao que recebe uma lista de numeros e retorna o numero de vezes que um elemento é igual ao anterior'''
    indice = 1
    contador = 0
    while indice <= len(lista):
        if lista[indice] == lista[indice-1]:
            contador += 1 
            indice += 1
        else:
            indice += 1
    return contador