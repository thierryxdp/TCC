# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''funçao que calcula e retorna se o colchao passara pela porta'''
    [a,b,c]=medidas
    if a<=L and b<=H or c<=H:
        return True
    if b>H and c<=L:
        return True
    else:
        return False