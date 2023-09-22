# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    porta=[[medidas[0],medidas[1],medidas[2]],h,l]
    if medidas[0]<h or medidas[0]<l or medidas[1]<h or medidas[1]<l or medidas[2]<h or medidas[2]<l:
        return True
    else:
        return False