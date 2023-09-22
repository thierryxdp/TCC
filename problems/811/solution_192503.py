def colchao(medidas, H , L):
    '''Dadas como entradas as medidas do colchão em ordem crescente 
    dentro de uma lista, a altura da porta e a largura da porta, 
    todas em centímetros.
    list, int, int --> bool'''
    Lmenor = medidas[0]
    Lmedio = medidas[1]
    return (Lmenor <= H or Lmenor <= L) and (Lmedio <= H or Lmedio <= L):