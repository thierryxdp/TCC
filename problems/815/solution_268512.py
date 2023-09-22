def insere(lista_numero,n):
    '''funcao que dado uma lista de ordem crescente adiciona um numero n na posicao correta
    list->list'''
    x=lista_numero
    x.append(n)
    y=list.sort(x)
    return y