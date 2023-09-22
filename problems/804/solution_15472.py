# Função que filtra os números pares inteiros de uma tupla
# tupla->tupla
# a, b, c, d são números inteiros quaisquer 
def filtra_pares(t_entrada):
    a=t_entrada[0]
    b=t_entrada[1]
    c=t_entrada[2]
    d=t_entrada[3]
    t=()
    if a%2==0:
        t=t+(a,)
    elif b%2==0:
        t=t+(b,)
    elif c%2==0:
        t=t+(c,)
    elif d%2==0:
        t=t+(d,)
        return t