def insere(lista_numero,n):
    ''' Função que recebe uma lista ordenada de números e um número inteiro n e inclui o número n na posição correta para que a lista continue ordenada; list,int->list'''
    l1=lista_numero
    list.append(l1,n)
    list.sort(l1)
    return l1