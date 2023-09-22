def faltante(lista):
    ''' '''
    contador=0
    intervalo=[]
    while contador<len(lista):
        list.sort(lista)
        intervalo=intervalo+list(range(1,lista[-1]))
        if intervalo[contador] != lista[contador]:
            contador=contador+1
            return intervalo[contador]