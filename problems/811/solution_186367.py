def colchao(medidas,H,L):
    """funcao que retorna True quando, dada as dimensões do colchão, o móvel passa pela porta e False quando não consegue.
    As dimensoes do colchão são postas em uma lista sendo o primeiro elemento a largura, depois a altura e por último o comprimento;
    list, float, float -> bool"""
    altura_colchao=colchao[0][2]
    largura_colchao=colchao[0][0]
    comprimento_colchao=colchao[0][1]
    if (largura_colchao<=L and comprimento_colchao<=H) or (largura_colchao<=L and altura_colchao<=H) or (altura_colchao<=L,comprimento_colchao<=H):
        return True
    else:
        return False