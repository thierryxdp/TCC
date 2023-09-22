# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    a,b,c = medidas
    if b > h or a > l:           
        return False
    else:
        return True