def maiores(lista,n):
    '''Função que retorna uma lista com números maiores
    que o número inteiro n.
    obs: a lista de entrada também é de números inteiros
    valores: list, int --> list'''
    lista.append(n)
    lista.sort()
    return lista[lista.index(n)+1:]

def acima_da_media(lista):
    '''Função que retorna uma lista ordenada das notas que
    ficaram acima da média.
    valores: list ---> list'''
    media = sum(lista)/len(lista)
    return maiores(lista,media)