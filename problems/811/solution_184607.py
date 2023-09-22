# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''colchao'''
    A,B,C= medidas
    if max(B,C)>max(H,L) and min(B,C)>min(H,L):
        return False
    else:
        return True