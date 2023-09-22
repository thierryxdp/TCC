def filtra_pares(s):
    """Função que recebe uma tupla com quatro elementos inteiros como 
    parâmetro, e retorna uma nova tupla contendo apenas os elementos 
    pares da tupla original na mesma ordem. Assinatura: tuple->tuple"""
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3]
    e=()
    if a%2==0:
        e=e+(,a)
    if b%2==0:
        e=e+(b,)
    if c%2==0:
        e=e+(c,)
    if d%2==0:
        e=e+(d,)
        return e
    else:
        return ()