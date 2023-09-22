# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """coment"""
    md=medidas
    if md[0]<=L and md[1]<=H or md[2]<=H and md[0]<=L or md[1]<=L and md[2]<=H:
        return True
    else:
        return False