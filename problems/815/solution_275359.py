def insere(lista_numero,n):
  '''Função que, dada uma lista ordenada de números inteiros e um número inteiro n, incluu n na posição correta, ou seja, de tal maneira que a lista continue ordenada
  list, int -> list'''

  lista_final = list.append(lista_numero,n)
  lista_ordenada = list.sort(lista_final)

  return lista_ordenada