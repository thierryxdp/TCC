def media(lista):
    '''media dos alunos'''
    return float(sum(lista)/len(lista))
def acima_da_media(lista):
    '''Dada uma lista com as notas dos alunos de uma turma;
    retorna uma lista ordenada com as notas acima de media;
    list => list'''
    list.append(lista,media(lista))
    list.sort(lista)
    if round(media(lista)) not in lista:
        if round(lista[0]) == round(media(lista)):
            return lista[0+1:]
        elif round(lista[1]) == round(media(lista)):
            return lista[1+1:]
        elif round(lista[2]) == round(media(lista)):
            return lista[2+1:]
        elif round(lista[3]) == round(media(lista)):
            return lista[3+1:]
        elif round(lista[4]) == round(media(lista)):
            return lista[4+1:]
        elif round(lista[5]) == round(media(lista)):
            return lista[5+1:]
        elif round(lista[6]) == round(media(lista)):
            return lista[6+1:]
        else:
            return lista[7+1:]
    if round(media(lista)) in lista:
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
        else:
            return lista[7+2:]