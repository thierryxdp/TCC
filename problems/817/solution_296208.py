def acima_da_media(notas):
    """dada uma lista com as notas dos alunos de uma
    turma, retorna uma lista ordenada com as notas
    que ficaram acima da media.
    list(float,float,...) -> list(float,float,...)"""
    media= sum(notas)/len(notas)
    list.sort(notas)
    list.append(notas,media)
    
    x = (list.index(notas,media)) + 1
    nova = notas[x:]
    
    return nova