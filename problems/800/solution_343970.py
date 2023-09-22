"""
A função recebe uma lista de compras e um dicionário com produtos e preços mapeados e retorna o valor total ao final da compra

Assinatura list, dict --> int
"""

def total(lista_de_compras,precos):

  """
  Para essa função foi declarada uma variável que será o total e depois usado um laço for com if para averiguar se o item da lista está ou não no dicionário e depois somar o preço a variável total e retorna ao final da averiguação da lista
  """

  total = 0

  for i in range(len(lista_de_compras)):

    if lista_de_compras[i] in precos:

      total = total + precos[lista_de_compras[i]]

  return round(total,2)