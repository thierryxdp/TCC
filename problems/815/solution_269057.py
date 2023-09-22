def insere(lista_numero,n):
   	'''Funcao que dado uma lista de numeros inteiros e um numero inteiro n retorna uma lista ordenada do maior ao menor que inclua o inteiro.
   list, int -> list'''
   lista = lista_numero+[n]
   list.sort(lista)
   return lista