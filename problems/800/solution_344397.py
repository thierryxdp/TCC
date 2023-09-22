def total(lista_de_compras,produtos):
  '''Função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis
  list, dict -> int'''

  soma_produtos = 0
  valor = 0

  for i in produtos.keys():
    if i in lista_de_compras:
      valor = dict.get(produtos,i)
      soma_produtos += valor
  return round(soma_produtos,2)