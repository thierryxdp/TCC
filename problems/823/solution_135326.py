def faltante(lista):
    '''retorna a peca que está faltando;
    list->int'''
    list.sort(lista)
    if not lista in 1:
        return [1]
    x=0
    while lista[x]==lista[x+1]-1:
        x=x+1
    return lista[x]+1