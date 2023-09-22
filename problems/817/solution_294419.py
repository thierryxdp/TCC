def acima_da_media(lista_notas):
    """
    Função que dada uma lista com as notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficaram acima da
    média.
    Parâmetro de Entrada: list
    Valor de Retoro: list
    """
	soma_das_notas= sum(lista_notas)
    numero_de_elementos=len(lista_notas)
    media_das_notas=soma_das_notas/numero_de_elementos
    list.sort(lista_notas)
    return lista_notas[list.index(lista_notas,media_das_notas+1):]