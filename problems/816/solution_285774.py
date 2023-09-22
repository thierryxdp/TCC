def maiores(n_int,n):
    '''Funcao que dada uma lista de numeros e um numero inteiro n, retorna outra lista que contem todos os numeros da lista original maiores que n, ordenados em ordem crescente
str->list,int
saida->list'''
    l_maior=[]
    for k in n_int:
        if k > n:
            l_maior.append(k)
    l_maior.sort()
    return l_maior