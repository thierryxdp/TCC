def repetidos(lista):
    """Fnção que recebe uma lista com numeros, retornado o numero de vezes
    que um elemento da lista é igual ao anterior
    entrada: lista
    retorno: int"""
    i= 0
    while i < len(lista):
        if i == 0:
            saida = 0
        else:
            if lista[i] == lista[i-1]:
                saida=saida + 1
        i= i+1
    return saida