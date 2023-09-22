def filtra_pares(a):
    lista=[]
    if type(a)==tuple and len(a)==4:
        for b in a:
            if b%2==0:
                lista.append(b)
                return lista