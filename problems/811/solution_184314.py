# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Função na qual dadas as medidas de um colchao diz se ele passa ou nao na porta do apartamento"""
    if min(medidas) <= L:
        medidas.remove(min(medidas))
        if min(medidas) <= H:
            return True
        else:
            return False