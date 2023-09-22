def acima_da_media(notas):
    '''funçao dado uma lista de notas de alunos faz a media e retorna os aprovados 
    list -> list'''
    aprovados = []
    media = sum(notas) / len(notas)
    for elemento in notas:
        if elemento > media:
            aprovados += [elemento]
    list.sort(aprovados)
    return aprovados