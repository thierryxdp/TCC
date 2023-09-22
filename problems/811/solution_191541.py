def colchao(medidas,h,l):
    '''funçao que dadas as medidas de um colchão em lista,
    espessura, largura, comprimento e altura e largura da
    porta, dizse é possível passar o colchão'''
    '(lista,h,l)=booleano'
    if medidas[1]<=l or medidas[1]<=h or medidas[2]<=l or medidas[2]<=h:
      return True
    else:
      return False