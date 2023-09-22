def acima_da_media(notas: list[float]) -> list[float]:
    '''recebe uma lista com notas dos alunos de uma turma e retorna uma lista 
    ordenada com as notas que ficaram acima da media'''
    media= sum(notas)/len(notas)
    copianotas= notas.copy()
    copianotas.append(media)
    copianotas.sort()
    posicaoN= copianotas.index(media)
    numerosMaiores = copianotas[posicaoN+1:]
    if media:
        if media in copianotas:
            quantidade = numerosMaiores.count(media)
            numerosMaiores = numerosMaiores[quantidade:]
    else:
        pass 
    return numerosMaiores