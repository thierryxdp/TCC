def acima_da_media(lista_notas):
  """dada uma lista como parametro, retorna outra lista com os elthos que estao acima da media entre eles
list->list"""
  media = sum(lista_notas)/len(lista_notas)
  return maiores(lista_notas, media)