def insere(lista_numero, n):
    """função que dada uma lista ordenada, inclua n na posição
    de modo que continue ordenada
    str -> str"""
  lista_numero.append(n)
  lista_numero.sort()
  return lista_numero