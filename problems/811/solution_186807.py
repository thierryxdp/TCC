def colchao(medidas,H,L):
    """Função que retorna a possibilidade de um colchao passar
    por uma porta dadas as medidas do colchao(em ordem crescente)
    e altura e largura da porta
    entrada: lista, int, int
    saida: booleano"""
    altura_col = medidas[0:1]
    largura_col = medidas[1:2]
    comprimento_col = medidas[2:]
    if comprimento_col >= H or L:
        return True
    elif largura_col >= H or L:
        return True
    if altura_col >= H or L:
        return True