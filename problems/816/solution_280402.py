def maiores(lista,n):
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    
  	lista_final = lista[posicao:]
    return lista_final