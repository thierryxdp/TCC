# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    if h>=medidas[1] or h>=medidas[2] or l>=medidas[1]:
        return True
    else:
        return False