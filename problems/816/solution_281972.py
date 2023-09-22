def maiores(lista,n):
      '''Dada uma lista e um valor para n, a funcao ira informar quais sao os
valores presente na lista maiores que n, os colocando  em ordem numerica list,int->list'''
      list.insert(lista,0,n)
      list.sort(lista)
      x =list.index(lista,n)
      return lista[x+1:]