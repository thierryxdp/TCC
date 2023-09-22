def insere(frase,n):
    '''função que recebe uma lista ordenada e um numero int, 
 e retorna uma nova lista ordenada em ordem crescente.
 list,int->list'''
    lista = list(frase)
    lista.append(n)
    list.sort(lista)
    return lista