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
    if b%2==0:
        t=t+(a,)+(b,)
    if c%2==0:
        t=t+(a,)+(b,)+(c,)
    if d%2==0:
        t=t+(a,)+(b,)+(c,)+(d,)
        return t