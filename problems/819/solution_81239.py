def filtraMultiplos(lista,n):
    '''
    retorna quais numeros da lista sao multiplos
    list -> n
    '''
    lista_multi=[]
    i=0
    while i<len(lista):
      if lista[i]%2==0:
        lista_multi=lista.append(lista[i])
        i=i+1
    return lista_multi