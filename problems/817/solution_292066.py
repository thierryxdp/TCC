def acima_da_media(notas):
    '''
    dada uma lista retorna uma lista ordenada com
    as notas que ficaram apenas acima da média
    entrada:lista
    saida:lista
    '''
    y=sum(notas)/len(notas)
    notas[0:0]=[y]
    list.sort(notas)
    x=list.index(notas,y)
    notas=notas[x+1:]
    if y in notas:
     	list.remove(notas,y)
    return notas
    else:
        return notas