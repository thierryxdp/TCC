def acima_da_media(lista):
    """Recebe uma lista com notas de alunos e retorna uma
lista ordenada com as notas maiores do que a média simples
da turma utilizando somatório e contagem do tamanho da lista.
list -> list
"""
    media = sum(lista)/len(lista)
    acima_media = maiores(lista, media)
    return acima_media