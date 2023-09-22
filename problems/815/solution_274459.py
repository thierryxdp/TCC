def insere(lista_numero,n):
    '''
    funcao que recebe uma lista em ordem crescente com
    numeros inteiros e um numero inteiro n e adiciona
    n na lista de forma que ela continue em ordem
    list,int->list
    '''
    lista_numero.append(n)
    crescente=sorted(lista_numero)
    return crescente