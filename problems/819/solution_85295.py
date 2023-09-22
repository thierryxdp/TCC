#retorna os multiplos de um número n
#list-->list
def filtraMultiplos(ls,n):
    lista=[]
    for x in ls:
        if x%n==0:
            lista.append(x)
    return lista