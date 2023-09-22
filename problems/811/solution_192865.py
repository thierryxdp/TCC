def colchao(medidas,H,L):
    '''Dada uma lista com as medidas da cama e a altura e largura da porta, retorna True se a medidas passa
assinatura: list, int, int --> str'''
    m=max(medidas)
    if m<=H:
        return True
    else:
        return False