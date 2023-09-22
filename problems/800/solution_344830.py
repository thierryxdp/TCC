def freq_palavras(frases):
    """Função recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja e retorna o valor total dos itens da lista que estejam disponíveis nesta loja """

  dicionario={}
  repeticoes = 0

  for palavra in frases.split(" "):
    repeticoes = list.count(frases.split(" "),palavra)
    dicionario[palavra] = repeticoes
  return dicionario