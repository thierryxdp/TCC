# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função que dado as medidas da porta e do colchão, retorna True para passa e False para não passa
    list, int, int --> bool"""
    lado_colchao = medidas[2]
    altura_colchao = medidas[1]
    if altura_colchao <= H or lado_colchao <= H and altura_colchao <= L or lado_colchao <= L:
        return True
    else:
        return False