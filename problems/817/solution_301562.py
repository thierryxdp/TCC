def acima_da_media(notas_alunos):
    '''Função que recebe uma lista com as notas dos alunos 
    e que retorna uma lista com as notas acimas da média
    int+>int'''
    soma=sum(nota)
    ni=len(nota)
    media=(soma//ni)
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
    return lista