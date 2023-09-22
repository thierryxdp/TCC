def acima_da_media(L):
    '''
       Funcao que recebe uma lista e retorna uma lista ordenada
       list -> list
    '''
       if n in lista:
          list.sort(lista)
          return lista[list.index(lista,n) + 1:]
       else:
         lista.insert(-1,n)
         list.sort(lista)
         return lista[list.index(lista,n) + 1:]
     
       media = int(sum(L)/len(L))
       return maiores(L,media)