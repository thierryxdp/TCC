# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    porta=[[medidas[0],medidas[1],medidas[2]],h,l]
    if medidas[0]<h and medidas[1]<h and medidas[2]<h or medidas[0]<l and medidas[1]<l and medidas[2]<l:
        return True
    else:
        return False