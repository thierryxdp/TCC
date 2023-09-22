#retorna uma segunda lista com números maiores que N de uma primeira lista
#str-->str
def maiores(a,b):
    c=[]
    for x in a:
        if x>b:
            list.append(c,x)
    list.sort(c)
    return c