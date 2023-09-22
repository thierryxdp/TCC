def acima_da_media(notas):
    '''
    funcao que retorna uma lista com as notas acima da media
    baseada em uma lista com as notas dos alunos da turma
    int->int
    '''
    soma=sum(notas)
    num=len(notas)
    media=int((soma/num)+1)
    list.append(notas,media)
    list.sort(notas)
    ordem_media= notas.index(media)
    return notas[ordem_media+1:]