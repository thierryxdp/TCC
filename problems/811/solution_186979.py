def colchao(medidas,H,L):
    if medidas[0]>=L or medidas[0]>=H:
        return False
    elif medidas[1]>L or medidas[1]>=H:
        return False 
    else:
        return True
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis