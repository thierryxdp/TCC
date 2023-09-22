def maiores(lista_numero, n):
  '''Função que recebe uma lista com números inteiros(lista_numero) e um número inteiro qualquer (n) e retorna
  uma nova lista, odrenada de forma crescente, que contenha, dos números da lista dada, apenas os números maiores que o número específicado
  list, int -> list'''
  lista_numero.append(n)
  lista_numero.sort()
  print(lista_numero)
  
  if max(lista_numero)>n:
   lista_numero = lista_numero[lista_numero.index(n)+1:]
  else:
    lista_numero = []
  return lista_numero