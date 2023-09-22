def insere(lista_numero, n):
    '''funcao que dada uma lista ordenada crescente de numeros inteiros e um numero inteiro n, inlcui n na posicao correta
    lista, int -> lista'''
    lista_numero = [n] + lista_numero
    return list.sort(lista_numero)