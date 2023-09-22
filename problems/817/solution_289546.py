def acima_da_media(lista,n):
    '''Recebe uma lista com as notas dos alunos de uma turma, retorna uma lista com as notas acima da média.
list -> list'''
    x = (sum(lista))/(len(lista))
    maiores_que = [numero for numero in lista if numero > x]
    list.sort(maiores_que)
    return maiores_que