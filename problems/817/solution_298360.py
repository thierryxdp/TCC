def maiores(lista,n):
      '''Dada uma lista e um ()valor para n, a funcao ira informar quais sao os
valores presente na lista maiores que n, os colocando  em ordem numerica'''
      list.insert(lista,0,n)
      list.sort(lista)
      x =list.index(lista,n)
      return lista[x+1:]
    
def acima_da_media(lista1):
    '''Dada uma lista, a funcao retornara na ordem
    os valores que sejam maiores q a média da lista'''
    c = sum(lista1)/len(lista1)
    return maiores(lista1,c)