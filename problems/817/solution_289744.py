def acima_da_media(notas):
    '''coment'''   
    notas= notas[:]+[funcao]
    list.sort(notas)
    funcao= sum(notas)/len(notas)
    ident= list.index(notas,funcao)
    
    return notas[ident+1:]