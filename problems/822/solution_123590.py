def repetidos(lista_numeros):
    '''Função que recebe uma lista de números e retorna quantas vezes um elemento da lista é igual ao elemento anterior;
    list -> int'''
    repeticoes = 0
    i = 1
    while i <len(lista_numeros):
        if lista_numeros[i] == lista_numeros[i-1]:
            repeticoes = repeticoes + 1
        i=i+1
    return repeticoes