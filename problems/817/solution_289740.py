def acima_da_media(notas):
    '''coment'''    
    notas[:]=notas
    list.sort(notas)
    funcao= sum(notas)/len(notas)
    list.index(funcao)