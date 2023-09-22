# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<=H and B<=H or A<=L and B<=L:#se um dos lados forem menores que a porta passa
        return True
    else:
        return False