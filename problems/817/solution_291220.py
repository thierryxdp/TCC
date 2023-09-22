def acima_da_media(lista):
    """função que recebe uma lista com as notas dos alunos de uma turma e retorna a média
    da turma e uma lista ordenada com as notas acima da média. list -> list"""
    media = round(sum(lista)/len(lista),2)
    maioresnotas = maiorquen(lista,media)
    list.sort(maioresnotas)
    return [media,maioresnotas]