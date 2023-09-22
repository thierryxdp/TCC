# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Calcula se o Colchão passa pela porta de João
       Entrada: medidas --> lista com A, B, C, representando as dimensões 
       			do colchão
                H --> altura da porta
                L --> Largura da porta"""
    medidas = list(medidas)
    A = medidas[0]
    medidas = [A,B,C]
    if ([C] <= H) and ([B] <= L):
        return True
    else:
        return False