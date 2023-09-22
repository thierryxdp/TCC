# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Funcao que retorna se é possivel passar o colchao pela porta. Str-->Bool"""
    list.sort(medidas, reverse = True)
    if((medidas[0] > H and medidas[1] > L) and (medidas[1] > H and medidas[0] > L)):
        return False
    else:
        return True