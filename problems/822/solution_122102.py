def repetidos(numeros):
    '''essa função recebe uma lista de numeros e retorna quando numeros são iguais aos seus antecessores'''
    '''list -> int'''
    i = int()
    cont = int()
    tamanho = len(numeros)
    while i<tamanho:
        if(numeros[i] == numeros[i-1]):
            cont +=1
        i +=1


    return cont