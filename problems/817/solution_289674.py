def acima_da_media(lista_de_notas):
    """Esta é a função que dada uma lista com a nota dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média, list -> list"""
    lista = sorted(lista_de_notas)
    return [i for i in lista if i >= 5]