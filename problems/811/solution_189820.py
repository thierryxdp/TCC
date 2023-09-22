# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    ''' Essa função define se um colção de altura(H) e largura(L) pode 
    entrar em uma porta de medidas[a,b,c]:
    lista, int, int, bool.'''
    
    if medidas[1]<= H:
        return True
    if medidas[1]<= L:
        return True
    else:
        return False