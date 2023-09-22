def acima_da_media(notas):
    '''funçao que dada uma lista com notas dos alunos de uma turma retorna 
    uma lista ordenada com as notas q ficaram acima da media'''
    Media = sum(notas)/len(notas)
    if Media in notas:
        return notas[notas.index(Media)+2:]
    notas.append(Media)
    notas.sort()
    return notas[notas.index(Media)+1:]