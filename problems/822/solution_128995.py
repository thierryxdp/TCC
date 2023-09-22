def repetidos(lista):
    '''funcao que dada uma lista numerica verifica a posicao de 
    um numero e retorna a quantidade de vezes que um elemento da lista 
    e igual ao elemento anterior
    list ->int'''
    indice = 0 
    contando = 0 
    repetindo = 0 
    while contando <len(lista):
        if lista [indice]==lista[indice-1]:
            repetindo = repetindo + 1
        indice = indice + 1
        contando = conatndo + 1
    return repetindo