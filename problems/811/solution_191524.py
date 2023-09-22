# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''funcao que verifica se um colchao consegue passar ppor uma porta;
    list, int, int -> bool'''
    #estou assumindo que o lado que passará paralelo ao chão será o de maior comprimento
    if medidas[1] >H or medidas[2] > L:
        return False
    elif medidas[1] <= H or medidas[2] <= L:
        return True
    elif medidas[2] >H or medidas[1] > L:
        return False
    elif medidas[2] <= H or medidas[1] <= L:
        return True