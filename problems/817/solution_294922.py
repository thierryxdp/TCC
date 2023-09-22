def acima_da_media(lista):
    ''' função que recebe uma lista com as notas dos alunos de uma turma e retorna uma lista com as notas acima da média;
    list -> list '''
    x = (sum(lista))/(len(lista))
    maiores_que_n = [numero for numero in lista if numero > x]
    list.sort(maiores_que_n)
    return maiores_que_n