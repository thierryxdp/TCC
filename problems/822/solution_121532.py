def repetidos(lista):
    '''funcao que recebe uma lista de numero como entrada e retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
    lista->int'''
    i=1
    repeticoes=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repeticoes = repeticoes +1
        i=i+1
    return n