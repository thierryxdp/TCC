def insere(lista_numero,n):
   "função que dada uma lista de números inteiros e um número n, retorna n em uma posição em que a lista continue crescente.list,float->list."
   lis = lista_numero
   list.insert(lis,-1,n)
   list.sort(lis)
   return lis