def acima_da_media(notas):
    '''Uma função acima da media que dada uma lista 
    com as notas dos alunos de uma turma, retorne
    uma lista ordenada com as notas que ficaram 
    acima da media. list[int] -> list[int]'''
    n = 4   
    numero = notas
    list.sort(notas)
    if notas[0] < n:
        return [i for i in notas if i >= n]
    else:
        return lista_numero