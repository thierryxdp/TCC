def maiores(lista_numeros, n):
  """dada uma lista como parâmetro e um inteiro, retorna outra lista com todos os valores maiores que o inteiro fornecido em ordem crescente
list,int->list"""
  lista = list(filter(lambda numero: numero > n, lista_numeros))
  lista.sort()
  return lista

print(maiores([7,2,3,4,5,6,1], 4))