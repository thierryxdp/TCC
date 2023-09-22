def repetidos(lista):
    '''dada uma lista de numeros, retorna o numero de vezes que um
    elemento da lista é igual ao elemento anterior
    list->int'''

    i = 1
    repeticoes = 0
    
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes