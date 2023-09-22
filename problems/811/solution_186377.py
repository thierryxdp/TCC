def colchao(medidas,H,L):
    """funcao que retorna True quando, dada as dimensões do colchão, o móvel passa pela porta e False quando não consegue.
    As dimensoes do colchão são postas em uma lista sendo o primeiro elemento a largura, depois a altura e por último o comprimento;
    list, float, float -> bool"""
    dimensoes_colchao=medidas
    altura_colchao=medidas[1]
    largura_colchao=medidas[0]
    comprimento_colchao=medidas[2]
    if (largura_colchao<=L and comprimento_colchao<=H) or (largura_colchao<=L and altura_colchao<=H) or (altura_colchao<=L and comprimento_colchao<=H) or (largura_colchao<=H and comprimento_colchao<=L):
        return True
    else:
        return False