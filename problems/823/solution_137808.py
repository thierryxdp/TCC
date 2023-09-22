def faltante(lista):
    '''Dada uma lista de números, descobrir qual número falta naquela ordem
    list->int'''
    contador=0
    i=0
    list.sort(lista)
    while i<len(lista):
        if 1 not in lista:
            return 1 
        #coloquei essa condição porque não importa quantas peças tenham, precisa da primeira
        if len(lista)==1 and lista[i]!=1:
            return lista[i]-1 
        if lista[i]+1 not in lista:
            return lista[i]+1
        i=i+1