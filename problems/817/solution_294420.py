def acima_da_media(lista_notas):
    """
    Função que dada uma lista com as notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficaram acima da
    média.
    Parâmetro de Entrada: list
    Valor de Retoro: list
    """
    list.sort(lista_notas)
	soma= sum(lista_notas)
    num_elemen=len(lista_notas)
    media=soma/num_elemen
    return lista_notas[list.index(lista_notas,media+1):]