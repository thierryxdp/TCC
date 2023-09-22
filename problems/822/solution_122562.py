def repetidos(lista):
    """função que recebe uma lista de numeros e retorna quantas repeticoes de numeros a lista contem"""
    repeticoes=0
    indice=0
    while indice<len(lista):
        if lista[indice]==lista[indice+1]:
            repeticoes= repeticoes +1
        indice= indice+1
    return repeticoes