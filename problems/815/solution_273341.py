def insere(lista_numero, n):
"""a função recebe um número e retorna uma lista com esse número na posição correta, sendo que está em ordem crescente;int->lista""" int->
  lista_numero.append(n)
  lista_numero.sort()
  return (lista_numero)