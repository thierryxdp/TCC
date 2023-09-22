def colchao(medidas,H,L):
  '''Função que, dadas as medidas (altura, largura, profundidade) de um colchão e a altura e largura de uma porta, calcula se o colchão de João passa pela porta de sua casa.
  list[int,int,int], int, int -> bool'''

  if medidas[1] <= L and medidas[0] <= H or medidas[1] <= H and medidas[0] <= L:
    #Se a largura do colchão for menor ou igual à largura da porta, e sua altura menor ou igual à altura da porta, o colchão entrará (deitado)
    #Se a largura do colchão for menor ou igual à altura da porta, e sua altura menor ou igual à largura da porta, o colchão entrará (em pé)
    return True 
  else:
    return False