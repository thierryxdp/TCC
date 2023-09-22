def acima_da_media (notas):
    'dadas as notas de alguns alunos, retorna as notas que ficaram acima da media. str ->str'
    qnotas = len(notas)
    media = sum(notas)/qnotas
    if media not in notas:
        list.append(notas, media)
        list.sort(notas)
        a = list.index(notas, media)
        return notas[a+1:]
    elif media in notas:
        list.sort(notas)
        a1 = list.index(notas, media)
        return notas[a1+1:]