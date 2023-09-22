def insere(lista_numero,n):
   	'''Dado uma lista ordenada de numeros itneiros e um numero inteiro n, a funcao inclui n na posição correta
    lis, int-> list'''
    lista= lista_numero+[n]
    list.sort(lista)
    return lista