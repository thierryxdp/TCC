def insere(lista_numero,n):
    '''função que dada uma lista(crescente) de números inteiros e um número inteiro n, retorne n na posição correta
    deixando a lista ordenada:
    string, int -> str'''
    l= lista_numero
    n= [n]
    x= l+n
    resposta= x.sort()
    return x