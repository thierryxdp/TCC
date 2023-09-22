def maiores(numeros_inteiros,n):
        '''retorna a lista, apos o n, em ordem crescente; lista,int -> list'''
        if n in numeros_inteiros:
            list.remove(numeros_inteiros,n)
        list.insert(numeros_inteiros,-1,n)
        list.sort(numeros_inteiros)
        return numeros_inteiros[list.index(numeros_inteiros,n)+1:]
def acima_da_media(notas):
    '''função que, dada uma lista com as notas dos alunos,
    retorna uma lista ordenada com as notas que ficaram 
    acima da média
    list-->list'''
    soma_notas = sum(notas)
    media_notas = soma_notas/len(notas)
    if media_notas in notas:
        notas_invertidas = sorted(notas,reverse=True)
        so_acima = notas_invertidas[0:list.index(notas_invertidas,media_notas)]
        return sorted(so_acima)
    else:
        return maiores(notas,media_notas)