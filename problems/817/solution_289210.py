def acima_da_media(x):
    '''Função que dada uma lista de alunos com suas respecitvas notas, retorna a media delas e de quem está acima da media
        list->list'''
    a=sum(x)/len(x)
    x.sort()
    b=x.index(x)
    return a,x[b+1:]