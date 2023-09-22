def faltante(lista):
    '''Função que dada uma lista com N-1 inteiros, retorna qual número inteiro está faltando
       list->int'''
    list.sort(lista)
    proximo=0
    pp=1
    while proximo<len(lista) and pp<len(lista):
        if lista[proximo]-lista[pp]==-2:
            return lista[proximo]+1
        proximo=proximo+1
        pp=pp+1
    if lista[0]==2:
        return 1
    else:
        return lista[proximo]+1