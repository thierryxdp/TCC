#Start your python function here
def filtra_pares(nome):
    """a,b,c,d=int"""
    mensagem=()
    if (nome%2==0):
        mensagem=mensagem+(nome[0],)
    if (nome%2==0):
        mensagem=mensagem+(nome[1],)
    if (nome%2==0):
        mensagem=mensagem+(nome[2],)
    if (nome%2==0):
        mensagem=mensagem+(nome[3],)
    return mensagem