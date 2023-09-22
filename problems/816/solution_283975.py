def maiores (lista, n):
    '''funcao que retorna outra lista que tem so numero maiores que n'''
  media = sum(lista) / len(lista)
  return media, len([n for n in lista if n > media])