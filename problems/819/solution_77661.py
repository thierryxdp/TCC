def filtraMultiplos(lista_n,n):
    ''' funcao retorna os multiplos de n presentes na lista'''
    i=0
    lista=[]
    while i+1<=len(lista_n):
        if int(lista_n[i])%n ==0:
            lista.append(lista_n[i])
        i+=1
    return lista