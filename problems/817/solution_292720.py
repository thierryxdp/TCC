def maiores(lista_inteiros,n):
    '''Função que recebe uma lista de números inteiros, um número inteiro n
        e retorna uma outra lista com todos os números da lista original que
        são maiores que n.'''
    list.insert(lista_inteiros,0,n)
    list.sort(lista_inteiros,reverse=True)
    x = list.index(lista_inteiros,n,0)
    del lista_inteiros[x::]

    return lista_inteiros[::-1]

def media(notas):
    '''Função que, dada uma lista com as notas de alunos de uma turma, retorna
        a média da turma e uma lista ordenada com as notas que ficaram acima
        da média.
        Entrada: list(int) ; Saída: list(int)'''
    media_notas = sum(notas)/len(notas)
    maiores_notas = maiores(notas,media_notas)

    return media_notas, maiores_notas