def maiores(lista,n):
    '''Essa função retorna uma lista ordenada em ordem crescente, onde os elementos são maiores que o paramêtro n,
    list->list'''
    list.sort(lista)
    for x in lista:
      if x<n:
        lista.remove(x)
      return lista