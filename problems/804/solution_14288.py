#Start your python function here
def filtra_pares(a,b,c,d):
    """a,b,c,d=int"""
    mensagem=()
    if (a%2==0):
        mensagem=mensagem+(a,)
    if (b%2==0):
        mensagem=mensagem+(b,)
    if (c%2==0):
        mensagem=mensagem+(c,)
    if (d%2==0):
        mensagem=mensagem+(d,)
    return mensagem