def repetidos(listi):
    '''Faça uma função chamada repetidos que receba como entrada uma lista de números,
     e retorne o número de vezes que um elemento da lista é igual ao elemento anterior.
        lista ->int'''
    i = 1
    repeticao = 0
    while i < len (listi):
        if listi [i] == listi [i -1]:
            repeticao +repeticao + 1
            i = i + 1
            return repaticao