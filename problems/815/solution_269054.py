def insere(lista_numero,n):
   	'''Funcao que inclui n na posição correta, dado uma lista ordenada de numeros inteiros e uma inteiro n e retorna uma lista ordenada do menor numero para o maior incluindo o numero inteiro
    lis, int -> list'''
    lista= lista_numero+[n]
    list.sort(lista)
    return lista