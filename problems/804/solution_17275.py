def filtra_pares(tupla):
    novatupla=()
    if tupla[0]%2==0:
        novatupla=novatupla+(tupla[0],)
    elif tupla[1]%2==0:
        novatupla=novatupla+(tupla[1],)
    elif tupla[2]%2==0:
        novatupla=novatupla+(tupla[2],)
    elif tupla[3]%2==0:
        novatupla=novatupla+(tupla[3],)
    return novatupla