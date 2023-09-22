def acima_da_media (listanotas):
    """Função que dada uma lista de notas dos alunos retorna uma outra lista
       com as notas ordenadas das quais ficaram acima da média.
       list->list
       
       Parâmetros:
       listanotas: lista das notas dos alunos de uma turma.
       
       returns: Uma nova lista com as notas que ficaram acima da média.
    """
    media = sum(listanotas) / len(listanotas)
    listanotas.append(media)
    listanotas.sort()
    return listanotas[listanotas.index(media) + 1:]