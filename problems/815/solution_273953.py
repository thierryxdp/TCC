def insere(lista_num,n):
    '''funçao que dada uma lista ordenada(crescente) de numeros 
    inteiros e um numero inteiro n, inclui n na posiçao correta na lista.
    list,int -> list'''
    lista_num.append(n)
    lista_num.sort()
    return lista_num