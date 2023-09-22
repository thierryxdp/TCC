# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao (medidas,H,L):
    if (H < medidas[0] or L > medidas[1] or H < medidas[2] or L > medidas[2]):
        return True
    elif (H < medidas[0] or L < medidas[1] or H < medidas[2] or L > medidas[2]):
        return True
    else:
        return False