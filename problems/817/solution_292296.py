def maiores(lista_inteiros,n):
    '''FunÃ§Ã£o que recebe uma lista de nÃºmeros inteiros, um nÃºmero inteiro n
        e retorna uma outra lista com todos os nÃºmeros da lista original que
        sÃ£o maiores que n.'''
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]

    return lista_inteiros[::-1]

def media(notas):
    '''FunÃ§Ã£o que, dada uma lista com as notas de alunos de uma turma, retorna
        a mÃ©dia da turma e uma lista ordenada com as notas que ficaram acima
        da mÃ©dia.
        Entrada: list(int) ; SaÃ­da: list(int)'''
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)