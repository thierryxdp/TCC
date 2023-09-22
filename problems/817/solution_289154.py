def acima_da_media(lista):
    """Dado uma lista com as notas dos alunos de uma turma, a função retorna uma nova lista com as notas que ficaram acima da média de notas da lista de entrada;
    list->list"""
    Nova_lista=lista[:]
    media=(((sum(Nova_lista))/(len(Nova_lista))))
    list.extend(Nova_lista,[media])
    list.sort(Nova_lista)
    indice=list.index(Nova_lista,media)+1
    del Nova_lista[:indice]
        return Nova_lista