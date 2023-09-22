def faltante(lista):
    '''retorna qual peça está faltando de um número de peças de 1 a N
    list->int'''
    i=0
    s=[]
    list.sort(lista)
    while i<len(lista)+1:
        s= s + [i+1,]
        i = i+1
    r = sum(s)
    t = sum(lista)
        return r-t