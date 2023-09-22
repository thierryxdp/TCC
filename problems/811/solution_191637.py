# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
    A = min(medidas[1:])
    B = max(H,L)
    C = False
    if B >= A:
        C = True
    return C