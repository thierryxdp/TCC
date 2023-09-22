def acima_da_media(lista_notas):
    '''Retorna uma lista ordenada com as notas de alunos de uma turma que ficaram
    acima da média aritmética de uma turma;
    entrada: lista;
    saída: lista:
    '''
    media_turma= sum(lista_notas)/len(lista_notas)
    if media_turma in lista_notas == False:
    	list.append(lista_notas,media_turma)
    list.sort(lista_notas)
    return lista_notas[list.index(lista_notas,media_turma)+1:]