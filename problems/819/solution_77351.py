def filtraMultiplos(l,n):
    ''''''
    lista=[]
    F = 0
    while l[F] in l:
        if l[F]%n:
            list.append(lista,l[F])    
        F = F + 1
    return lista