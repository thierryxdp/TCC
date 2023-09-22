def maiores(lista,n):
      list.insert(lista,0,n)
      list.sort(lista)
      x =list.index(lista,n)
      return lista[x+1:]