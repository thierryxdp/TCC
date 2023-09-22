def acima_da_media(lista):
    """ dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas acima da média das notas
    list -> list"""
   	media = sum(lista)//len(lista)
    return media