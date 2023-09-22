tupla=(1,2,3,4)
def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos inteiros
    como parâmetro e retorna uma nova tupla contendo apenas 
    elementos pares da tupla original, na mesma ordemem que se 
    encontravam."""
    a=int(tupla[0])
    b=int(tupla[1])
    c=int(tupla[2])
    d=int(tupla[3])
    t=()
    if a%2==0:
        t=t+(a,)
    if b%2==0:
        t=t+(b,)
    if c%2==0:
        t=t+(c,)
    if d%2==0:
        t=t+(d,)
    return t