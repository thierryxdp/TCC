def maiores(inteiros,n):
    '''A funcao recebe uma lista de inteiros e um numero n e retorna uma lista com
todos os numeros maiores do que n na lista de inteiros
list,int->list'''
    inteiros.append(n)
    inteiros.sort()
    lista=inteiros[n+1:]
    return lista