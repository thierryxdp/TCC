# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    [a,b,c] = medidas    
    
    if a and b and c > h and l:
        return False
    else:
        return True