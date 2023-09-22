def maiores_que(lista_numero, n):
  '''Função que recebe uma lista com números inteiros(lista_numero) e um número inteiro qualquer (n) e retorna
  uma nova lista, odrenada de forma crescente, que contenha, dos números da lista dada, apenas os números maiores que o número específicado
  list, int -> list'''
  lista_numero.append(n)
  lista_numero.sort()
  
  if max(lista_numero)>n:
   lista_numero = lista_numero[lista_numero.index(n)+1:]
  else:
    lista_numero = []
  return lista_numero


def acima_da_media(notas):
  '''Função que recebe as notas(notas) dos alunos de uma sala em forma de lista e retorna
  uma nova lista, apenas com valores que, das notas dos alunos da sala, sejam maiores que a média dessas notas
  list -> list'''
  media = sum(notas)/len(notas)
  return maiores_que(notas,media)
acima_da_media([6,6])