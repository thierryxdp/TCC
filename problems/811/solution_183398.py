# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    "Dadas as medidas de um colchão e uma porta, retorna True caso o colchão consiga passar pela porta e False caso não consiga. float, float, float, float, float - > str"
    if medidas[0]<=L and medidas[1]<=H: 
        return True
    elif medidas[2]>H or medidas[1]>L:
        return False