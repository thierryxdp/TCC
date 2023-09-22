def colchao(medidas, H, L):
    """Função que dadas as dimensões de colchão (A, B, C) que João pretende comprar e as dimensões da porta(H, L), nos diz se o colchão em questão passa ou não pela porta, considerando que João pode arrastá-la pelo chão com uma das faces do colchão paralela ao chão. 
    (list, int, int) -> bool"""

    medidas_em_ordem = sorted(medidas)

    porta = (H, L)

    dimensoes_porta = list(porta)

    dimensoes_porta_em_ordem = sorted(dimensoes_porta)

    if medidas_em_ordem[0] <= dimensoes_porta_em_ordem[0] and medidas_em_ordem[1] <= dimensoes_porta_em_ordem[1]:
        return True

    else:
        return False