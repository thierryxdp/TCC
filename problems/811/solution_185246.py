# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a,b,c=medidas
    if a<=L and b<=H or a<=H and b<=L:
        return True
    else:
        return False