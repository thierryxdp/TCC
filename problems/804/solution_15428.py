# Função que filtra os números pares inteiros de uma tupla
# tupla->tupla
# a, b, c, d são números inteiros quaisquer 
def filtra_pares(a,b,c,d):
    t=()
    if a%2==0:
        t=t+(a,)
    elif b%2==0:
        t=t+(a,)+(b,)
    elif c%2==0:
        t=t+(a,)+(b,)+(c,)
    elif d%2==0:
        t=t+(a,)+(b,)+(c,)+(d,)
        return t