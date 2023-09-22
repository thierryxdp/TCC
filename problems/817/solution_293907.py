def acima_da_media (lista):
    ''' funcao que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da media;
lista -> lista '''
    x = (sum(lista))/(len(lista))
    maiores_que = [numero for numero in lista if numero > x]
    list.sort(maiores_que)
    return maiores_que