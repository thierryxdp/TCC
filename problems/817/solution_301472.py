def maiores(lista_numeros, n):
  """dada uma lista como parâmetro e um inteiro, retorna outra lista com todos os valores maiores que o inteiro fornecido em ordem crescente
list,int->list"""
  lista = list(filter(lambda numero: numero > n, lista_numeros))
  lista.sort()
  return lista




def acima_da_media(lista_notas):
  """dada uma lista como parametro, retorna outra lista com os elthos que estao acima da media entre eles
list->list"""
  media = sum(lista_notas)/len(lista_notas)
  return maiores(lista_notas, media)