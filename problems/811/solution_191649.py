# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    if medidas[0]<H or L and medidas[1]<H or L:    
        return True
    else:
        return False