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
    if(len(notas)>1):
        media = (sum(notas))/(len(notas))
        Nmaiores = maiores(notas,media)
        if (Nmaiores[0] == media):
            return Nmaiores[1:]
        else:
            return Nmaiores
    else:
        return []