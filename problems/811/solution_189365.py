# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    if medidas[0]<h and medidas[1]<l or medidas[0]<l and medidas[1]<h:
        return True
    if medidas[0]<h and medidas[2]<l or medidas[0]<l and medidas[2]<h:
        return True
    if medidas[2]<h and medidas[1]<l or medidas[2]<l and medidas[1]<h:
        return True
    else:
        return False