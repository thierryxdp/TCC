def acima_da_media (lista):
    ''' funcao que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da media;
list -> list '''
    a = (sum(lista))/(len(lista))
    b = [numero for numero in lista if numero > x]
    list.sort(b)
    return b