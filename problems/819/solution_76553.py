def filtraMultiplos(lista_n,n):
    i=0
    lista_r=[]
    while i<len(lista_n):
        if lista_n[i]%n==0:
            lista_r.append(lista_n[i])
        i=i+1
    return lista_r