# Função que filtra os números pares inteiros de uma tupla
#tupla->tupla
#a,b,c, d são números inteiros quaisquer 
def filtra_pares(a,b,c,d):
    t=()
    if a/2==0:
        return t+(a,)
    elif a/2!=0:
        return t+()
    if b/2==0:
        return t+(b,)
    elif a/2!=0:
        return t+()
    if c/2==0:
        return t+(c,)
    elif c/2!=0:
        return t+()
    if d/2==0:
        return t+(d,)
    elif d/2!=0:
        return t+()