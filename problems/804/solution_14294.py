#Start your python function here
def filtra_pares(nome):
    """a,b,c,d=int"""
    mensagem=()
    if (int(nome)%2==0):
        mensagem=mensagem+(int(nome[0]),)
    if (int(nome)%2==0):
        mensagem=mensagem+(int(nome[1]),)
    if (int(nome)%2==0):
        mensagem=mensagem+(int(nome[2]),)
    if (int(nome)%2==0):
        mensagem=mensagem+(int(nome[3]),)
    return mensagem