def repetidos(lista):
    """Função que recebe uma lista de numeros e retorna o numero de vezes
    que um elemento da lista é igual ao elemento anterior,lista-->lista"""
    i=0
    repeticoes=0
    while (i<len(lista)-1):
        if (lista[i+1]==lista[i]):
            repeticoes+=1
        i+=1
    return repeticoes