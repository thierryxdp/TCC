def repetidos(lista):
    ''' '''
    bloco=[]
    contador=0
    while contador < len(lista):
        anterior=contador-1
        if lista[contador]==lista[anterior]:
            bloco=bloco+[lista[contador]]
        contador=contador+1
    return (len(bloco))