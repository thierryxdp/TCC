def acima_da_media(lista):
    """ dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas acima da média das notas
    list -> list"""
    list.sort(lista)
    indice = sum(lista)//len(lista)
    lista = lista[indice:]
    return lista