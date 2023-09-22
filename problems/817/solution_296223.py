def acima_da_media(notas):
    """dada uma lista com as notas dos alunos de uma
    turma, retorna uma lista ordenada com as notas
    que ficaram acima da media.
    list(float,float,...) -> list(float,float,...)"""
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    
    x = (list.index(notas,media)) + 1
    notas = notas[x:]
    
    if media in notas:
        notas=notas[x+1:]
   
    return notas