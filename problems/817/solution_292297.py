def media(notas):
    '''Funcao que dada uma lista com as notas de alunos de uma turma, retorna
        a media da turma e uma lista ordenada com as notas que ficaram acima
        da media.
        Entrada: list(int) ; Saída: list(int)'''
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)

    return maiores_notas