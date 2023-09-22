# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    
    A,B,C = medidas
    
    if H*L > A*B:  
        return true
    
    elif H*L > B*C:
        return true
    
    else:
        return false