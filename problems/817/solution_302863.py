def maiores(numeros,n):
    '''Recebe uma lista e um elemento n e retorna uma nova lista com
    todos os elementos maiores do que n (list, int -> int)'''
    list.append(numeros,n)
    list.sort(numeros)
    posicao_n = numeros.index(n)
    return numeros[posicao_n + 1 : ]
def acima_da_media (notas):
    '''Recebe uma lista com as notas dos alunos de uma turma e retorna
    quais delas ficaram acima da média da turma (list -> list)'''
    if len(notas) > 1:
        media = sum(notas)/len(notas)
        return maiores(notas,media)
    else:
        return []