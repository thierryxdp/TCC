# Dada uma lista de notas de uma turma,
# retorna uma lista ordenada com as notas que ficaram acima da média
# list -> list
def acima_da_media(lista):
    media = sum(lista) / len(lista)
    return maiores(lista, media)