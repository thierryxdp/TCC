def total(compras, preco):
    '''Retorna o valor total dos itens de uma lista
    que estejam disponiveis em uma loja.
    list, list -> int'''
    valor = 0
    for i in compras:
      if i in preco:
        valor += preco[i]
    return round(valor,2)