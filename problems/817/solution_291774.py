'''Recebe uma lista de notas de alunos e retorna as notas que ficaram acima da média
list -> list'''
def acima_da_media(notas):
    media = sum(notas)/len(notas)
    acima = []
    for nota in notas:
        if nota > media:
            acima.append(nota)
    acima.sort()
    return acima