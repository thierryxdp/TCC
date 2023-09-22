def maiores(lista,n):
    '''funcao que dada uma lista de inteiros e um numero inteiro n, retorna outra lista com 
    todos os numeros maiores que n ordenados em ordem crescente
    list,int->list
    '''
    lista.append(n)
    lista.sort()
    x=lista.find(n)
    return lista[x:]