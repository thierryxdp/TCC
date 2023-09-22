def faltante(lista):
    '''Retorna o número da peça faltante do quebra-cabeça de Joãozinho
list -> int'''
    listabackup=lista[:]
    listacompleta=list(range(1,len(lista)+1))
    list.sort(listabackup)
    i=0
    faltante=0
    while i<len(listabackup):
        if listabackup[i]!=listacompleta[i]:
            faltante=faltante+listacompleta[i]
            return faltante
        i=i+1
    else:
            faltante=listacompleta[-1]+1
            return faltante