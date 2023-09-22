# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ funçao que calcula o tamanho do colchao dados as medidas e retorna True se passar pela porta e False se nao passar;
    int->bool"""
    if L >= medidas[0] and H >= medidas[1]:
        return True
    else:
        return False