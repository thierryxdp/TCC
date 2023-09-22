def maiores(numeros, n):
    '''Funcao recebe uma lista contendo numeros interios e um numero qualquer e retoena os numeros que são maiores que esse outro numero qualquerr
Lista/int -> Lista'''
    listaN = (numeros + [n])
    list.sort(listaN)
    posicao = list.index(listaN, n)
    return listaN[posicao+1:]

def acima_da_media(notas):
    '''Funcao recebe uma lista cotendo uma lista contendo as notas de uma turma e retorna uma lista com todas as notas que ficaram acima da média
lista -> lista'''
    media = (sum(notas))/(len(notas))   
    return maiores(notas,media)