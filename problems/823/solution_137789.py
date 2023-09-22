def faltante(lista):
    '''Dada uma lista de números, descobrir qual número falta naquela ordem
    list->int'''
    contador=0
    i=0
    while i<len(lista):
        if (lista[(len(lista)-1)])>lista[i] and lista[i]+1 not in lista:
            return lista[i]+1
        if (lista[(len(lista)-1)])<lista[i] and lista[i]-1 not in lista: 
            return lista[i]-1
        i=i+1