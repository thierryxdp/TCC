def insere(lista_numero, n):
    """a função retorna uma lista de números em ordem crescente; int->list"""
  lista_numero.append(n)#insere numero na lista 
  lista_numero.sort()#ordena a lista novamente
  return lista_numero