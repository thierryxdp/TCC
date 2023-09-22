# Função que filtra os números pares inteiros de uma tupla
#tupla->tupla
#a,b,c, d são números inteiros quaisquer 
def filtra_pares(a,b,c,d):
    t=()
    if a/2==0:
        t+(a,)
    elif a/2!=0:
        t+()
    if b/2==0:
        t+(b,)
    elif a/2!=0:
        t+()
    if c/2==0:
        t+(c,)
    elif c/2!=0:
        t+()
    if d/2==0:
        t+(d,)
    elif d/2!=0:
        return t+()