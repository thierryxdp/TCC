def colchao(medidas,H,L):
    """Função que retorna a possibilidade de um colchao passar
    por uma porta dadas as medidas do colchao(em ordem crescente)
    e altura e largura da porta
    entrada: lista, int, int
    saida: booleano"""
    altura_col = medidas[0:1]
    largura_col = medidas[1:2]
    comprimento_col = medidas[2:]
    if (comprimento_col <= [H] or comprimento_col <= [L]) and (altura_col <= [H] or altura_col <= [L]):
        return not False 
    elif (largura_col <= [H] or largura_col <= [L]) and (comprimento_col <= [H] or comprimento_col <= [L]):
        return not False
    if (altura_col <= [H] or altura_col <= [L]) and (largura_col <= [H] or largura_col <=  [L]):
        return not False
    else:
        return False