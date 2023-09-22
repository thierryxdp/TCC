# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis a*b<h*l
def colchao(medidas,h,l):
    a, b, c = medidas
    if(a<=min(h,l) and b<=max(h,l)):
        return True
    else:
        return False