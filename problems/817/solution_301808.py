def maiores(lista,n):

  nova_lista = []

  for i in range(len(lista)):

    if lista[i] > n:

      nova_lista = nova_lista + [lista[i]]

  nova_lista_ordenada = sorted(nova_lista)

  return nova_lista_ordenada

"""
A função recebe apenas uma lista com as notas da turma e deve retornar outra lista apenas com as notas acima da média

Assinatura: list --> list
"""

def acima_da_media(notas):

  """
  Para isso primeiro eu tirei a média das notas usando a função "sum" que dá a soma dos valores da lista dividida pela função "len" que retorna o número de elementos da lista

  Em seguida eu usei a função anterior para selecionar apenas os valores acima da média calculada
  """

  media = sum(notas)/len(notas)

  lista_final = maiores(notas,media)

  return lista_final