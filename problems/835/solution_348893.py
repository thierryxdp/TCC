def melhor_volta(n):
    '''Dado uma matriz(n) 6x10 contendo o tempo de 10 voltas de 6 corredores,
    retorna uma tupla com menor tempo de volta, posição do corredor na matriz
    e numero da volta.list(list)->tuple'''
    k=min(n[0]),min(n[1]),min(n[2]),min(n[3]),min(n[4]),min(n[5])
    p=min(k)
    l=k.index(p)
    j=n[l].index(p)
    return (l+1,p,j+1)