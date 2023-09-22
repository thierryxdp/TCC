def acima_da_media(notas):
    '''coment'''   
    if notas>=3:
    list.sort(notas)
    funcao= sum(notas)/len(notas)
    ident= list.index(notas,funcao)
    
    return notas[ident+1:]