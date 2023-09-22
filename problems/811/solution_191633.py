# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
    
    A,B,C = medidas
    
    if A*B < H*L:
        return True
    
    elif A*C < H*L:
        return True
    
    elif B*C < H*L:
        return True
    
    else:
        return False