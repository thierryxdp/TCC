def faltante(lista):
    '''retorna a peca que está faltando;
    list->int'''
    list.sort(lista)
    if lista[0]!=1:
        return 1
    if len(lista)==lista[-1]-1:
        return lista[-1]+1
    x=0
    while lista[x]==lista[x+1]-1:
        x=x+1
    return lista[x]+1