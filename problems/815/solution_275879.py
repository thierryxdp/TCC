def insere(lista_numero, n):
  '''Função que recebe uma lista ordenada de forma crescente com números inteiros(lista_numero) e um número inteiro qualquer (n) e retorna
  uma nova lista na qual foi inserido o número n na posição correta, de forma ordenada 
  list, int -> list'''
  lista_numero.append(n)
  lista_numero.sort()
  return lista_numero