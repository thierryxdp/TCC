def maiores (inteiros,n):
    '''
    função que recebe uma lista de inteiros e un numero n,
    e retorna outra lista que tenha os numeros da lista 
    original maiores que  n, ordenados na ordem crescente
    list,int->list
    '''
    list.append(inteiros,n)
    list.sort(inteiros)
    a = len(inteiros)
    b = list.index(inteiros,n)
    return inteiros[b+1:a]