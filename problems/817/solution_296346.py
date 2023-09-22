def acima_da_media (notas):
    '''
       Função que recebe uma lista com as notas dos alunos de
       uma turma (lista) e retorna uma lista ordenada com as
       notas que ficaram acima da media;
       list -> list
    '''
    if media not in notas:
        media = sum(notas)/len(notas)
        notas.append(media)
        notas.sort()
        del notas[:notas.index(media)]
        notas.remove(media)
        return notas
    else:
        media = sum(notas)/len(notas)
        notas.append(media)
        notas.sort()
        del notas[:(notas.index(media)+1)]
        notas.remove(media)
        return notas