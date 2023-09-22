# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    [a,b,c] = medidas    
    
    if  b <= h or c <= l:
        return True
    else:
        return False