# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao (medidas,h,l):
    porta=h*l
    if medidas[0]>h or medidas[0]>l or medidas[1]>h or medidas[1]>l:
        return False
    elif medidas[0]>h or medidas[0]>l or medidas[2]>h or medidas[2]>l:
        return False
    elif medidas[2]>h or medidas[2]>l or medidas[1]>h or medidas[1]>l:
        return False
    else:
        return True