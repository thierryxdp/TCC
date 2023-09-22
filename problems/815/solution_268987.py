def insere(lista_numero,n):
    """ Insere um numero n em uma lista e arruma todos os numeros em ordem
crescente dentro da lista.
list,int-->list
  """
    lista_numero.append(n)    
    list.sort(lista_numero)
    
    return lista_numero