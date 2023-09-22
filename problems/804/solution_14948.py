def filtra_pares(nome):
    mensagem=()
    if (nome[0]%2=0):
        mensagem=mensagem+(nome[0],)
    if (nome[1]%2==0):
        mensagem=mensagem+(nome[1],)
    if (nome[2]%2==0):
        mensagem=mensagem+(nome[2],)
    if (nome[3]%2==0):
        mensagem=mensagem + (nome[3],)
        return mensagem