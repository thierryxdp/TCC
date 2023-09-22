def media(lista):
    '''media dos alunos'''
    return int(sum(lista)/len(lista))
def acima_da_media(lista):
    '''Dada uma lista com as notas dos alunos de uma turma;
    retorna uma lista ordenada com as notas acima de media;
    list => list'''
    list.append(lista,media(lista))
    list.sort(lista)
    if lista[0] == round(media(lista)):
        return lista[0+2:]
    elif lista[1] == round(media(lista)):
        return lista[1+2:]
    elif lista[2] == round(media(lista)):
        return lista[2+2:]
    elif lista[3] == round(media(lista)):
        return lista[3+2:]
    elif lista[4] == round(media(lista)):
        return lista[4+2:]
    elif lista[5] == round(media(lista)):
        return lista[5+2:]
    elif lista[6] == round(media(lista)):
        return lista[6+2:]