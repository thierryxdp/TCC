# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    m=sorted(medidas)
    m1=m[0]
    m2=m[1]
    m3=m[2]
        
    if m1<H and m3<L:
        return True 
    elif m1<H and m3>L:
        return False
    elif m1<H and m3==L:
        return False
    elif m1>H and m3<L:
        return False
    elif m1==H and m3<L:
        return False
    elif m1>H and m3>L:
        return False
    elif m1==H and m3==L:
        return False