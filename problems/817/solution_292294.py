def media(notas):
    '''FunÃ§Ã£o que, dada uma lista com as notas de alunos de uma turma, retorna
        a mÃ©dia da turma e uma lista ordenada com as notas que ficaram acima
        da mÃ©dia.
        Entrada: list(int) ; SaÃ­da: list(int)'''
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)

    return maiores_notas