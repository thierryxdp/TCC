# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Calcula se o Colchão passa pela porta de João
       Entrada: medidas --> lista com A, B, C, representando as dimensões 
       			do colchão
                H --> altura da porta
                L --> Largura da porta"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if (C <= H) and (A <= L):
        return True
    else:
        return False