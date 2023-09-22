# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medida, H, L):
    colchao_alt = medida[1]
    colchao_larg = medida[2]
    colchao_comp = medida[0]
    if colchao_alt < H or colchao_larg < L:
        return True