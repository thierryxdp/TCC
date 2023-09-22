def repetidos(lista):
    """Fnção que recebe uma lista com numeros, retornado o numero de vezes
    que um elemento da lista é igual ao anterior
    entrada: lista
    retorno: int"""
    saida = 0
    i= 0
    while i< len(lista):
        if lista[i] == lista[i+1]:
            saida= saida+ 1
        if i == len(lista):
            return 'fim da lista'
        i= i+1
    return saida