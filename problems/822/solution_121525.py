def repetidos(lista):
    '''funcao que recebe uma lista como entrada e retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
    lista->int'''
    i=0
    n=i+1
    repeticoes=' '
    while i<len(lista):
        if lista[i]==lista[n]:
            repeticoes=(repeticoes)+1
        i=i+1
    return repeticoes