# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    #A - largura B- comprimento C- altura
    #H - altura L- largura 
    # B < L or C < H 
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if B < L or C < H:
        return True
    else:
        return False