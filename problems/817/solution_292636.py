def acima_da_media(lista: list) -> list:
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista
       ordenada com as notas dos alunos que ficaram acima da média da turma

       Parameters:
       lista: Lista contendo as notas dos alunos de uma turma

       Return:
       Dado o parâmetro "lista", retorna uma nova lista, ordenada em ordem
       crescente, com as notas dos alunos que ficaram acima da média aritmética
       da turma

       Examples:
       acima_da_media([10, 2]) == [10]
       acima_da_media([2, 4, 8]) == [8]
       acima_da_media([1, 2, 3, 7, 8, 8.5]) == [7, 8, 8.5]
    """

    x = (sum(lista)) / (len(lista))
    list.append(lista, x)
    list.sort(lista)
    y = list.index(lista, x)
    z = lista[y + 1:]

    return z