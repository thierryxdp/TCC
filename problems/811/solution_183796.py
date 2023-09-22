# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H,L):
    [m1,m2,m3]=medidas
    if ((m2>H and m3>L) or (m2>L and m3>H) ) and (m1>L):
        return False
    else:
        return True