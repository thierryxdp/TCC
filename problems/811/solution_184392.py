# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,H,L):
    '''Retorna verdadeiro caso o colchao passe e falso caso nao passe'''
    
    if H>L:
        return medidas[0] <= L and medidas[1] <= H
    else:
        return medidas[0] <= H and medidas[1] <= L