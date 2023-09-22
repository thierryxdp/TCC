def acima_da_media(notas):
    '''
    funcao retorna uma lista c as notas acima da media
    '''
    x=sum(notas)/len(notas)
    green=list()
    for h in notas:
        if h>x:
            green.append(h)
            list.sort(green)
    return green