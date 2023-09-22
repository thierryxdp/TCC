def acima_da_media(notas):
    '''
    dada uma lista contendo as notas dos alunos,
    retorna as notas que ficaram acima da média
    da turma
    
    list -> list
    '''
    
    import math
    media = math.ceil(sum(notas)/len(notas))
    if media in notas:
        notas.sort()
        x = notas.index(media)
        output = notas[x+1:]
        return output
    else:
        notas.append(media)
        notas.sort()
        x = notas.index(media)
        output = notas[x+1:]
        return output