'''Recebe uma lista de notas de alunos e retorna as notas que ficaram acima da média
list -> list'''
def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return maiores(notas,media)