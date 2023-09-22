def maiores(lista_inteiros,n):
    '''Retorna uma lista contendo somente os números de uma lista prévia
    de valores maiores que o de um número inteiro n;
    entradas: lista, int;
    saída: int;
    '''
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    return lista_inteiros[list.index(lista_inteiros,n)+1:]
def acima_da_media(lista_notas):
    '''Retorna uma lista ordenada com as notas de alunos de uma turma que ficaram
    acima da média aritmética de uma turma;
    entrada: lista;
    saída: lista;
    '''
    media_turma= sum(lista_notas)/len(lista_notas)
    maiores(lista_notas, media_turma)
    i = list.index(lista_notas,media_turma)+ list.count(lista_notas,media_turma)
    return lista_notas[i:]