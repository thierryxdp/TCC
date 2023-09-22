def filtraMultiplos(lista,n):
    'dada uma lista com numeros retorne os multiplos de n desta lista.list,int-->list'
    multiplos=[]
    indice=0
    while indice<len(lista):
        if lista[indice]%n==0:
            list.append(multiplos,lista[indice])
        indice=indice+1
    return multiplos