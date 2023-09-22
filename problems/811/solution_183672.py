# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que identifica se um colchão com suas respectivas medidas são capazes de passar por uma porta de medidas H e L (altura e largura)
    list, int, int -> bool"""
    x = medidas
    if H>L and x[0]<=L and x[1]<=H :
        return True
    else:
        return False
    if H<L and x[0]<=H and x[1]<=L :
        return True
    else:
        return False