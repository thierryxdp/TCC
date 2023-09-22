# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    x = medidas
    if H>L and x[0]<L and x[1]<H:
        return true
    else:
        return false
    if H<L and x[0]<H and x[1]<L:
        return true
    else:
        return false