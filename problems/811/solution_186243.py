# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    
    colchao=medidas[1]*medidas[2]
    porta= H*L
    
    if colchao> porta:
        return 'false'
    if colchao<= porta:
        return 'true'