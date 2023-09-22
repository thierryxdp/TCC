def filtra_pares(tupla):
    if tupla == ():
        return ()
    else:
        novatupla = ()
        i = 0
        while i < len(tupla):
            if tupla[i]%2 == 0:
                novatupla = novatupla + (tupla[i],)
            i+=1
        return novatupla