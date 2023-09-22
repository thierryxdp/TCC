def maiores(lista,n):
    '''
    funcao que recebe uma lista de numeros inteiros e um
    numero inteiro n e retorna uma outra lista com todos
    os numeros maiores que n em ordem crescente
    list,int->list
    '''
    lista.append(n)
    crescente=sorted(lista)
    posicao=crescente.index(n)
    return crescente[posicao+1:]