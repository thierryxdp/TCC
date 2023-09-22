def repetidos(lista):
    '''funcao que recebe uma lista como entrada e retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
    lista->int'''
    while i<len(lista):
        n=i+1
        i=0
        if lista[i]==lista[n]:
            a=a+1
        i=i+1
    return a