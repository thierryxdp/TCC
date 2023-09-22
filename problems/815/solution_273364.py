def insere(lista_numero,n):
   '''funcao que dada uma lista em ordem crescente de numeros inteiros e um numero inteiro n, inclua n na posicao correta. list->list'''
   lis = lista_numero
   list.insert(lis,-1,n)
   list.sort(lis)
   return lis