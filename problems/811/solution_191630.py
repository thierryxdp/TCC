# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    
    A,B,C = medidas
    
    if H*L > A*B:  
        return True
    
    elif H*L > B*C:
        return True
    
    else:
        return False