# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas, H, L):
    '''
    Por meio das medidas do colchao de uma dada porta,
    a função verifica se é possivel passar o colchao pela porta.
    
    list, float, float -> bool
    '''
    if H > L: #Faz com que H seja sempre menor ou igual que L para facilitar a comparacao
        H, L = L, H
 
    medidas = sorted(medidas)
    return medidas[0] <= H and medidas[1] <= L