def repetidos(lista):
    '''Função chamada repetidos que receba como entrada uma lista de números, e retorne o número
de vezes que um elemento da lista  ́e igual ao elemento anterior;list->int'''
    ind=0
    qtd_repetidos=[]
    while ind<len(lista):
        if lista[ind]==lista[ind+1]:
        	qtd_repetidos.append(lista[ind])
        ind=ind+1
    return len(qtd_repetidos)