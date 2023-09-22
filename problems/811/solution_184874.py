# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que dados as medidas de um colchao compradado com altura e largura das portas da casa de joão conseguimos definir se o colchao a comprar e o certo.
    parametros: list,int,int->bool"""
    A = medidas[0]
    B = medidas[1]
    if (B <= H and A <= L) or (B <= L and A <= H):
        return True
    else:
        return False