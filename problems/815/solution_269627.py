def insere(lista_numero, n):
    '''Recebe uma lista ordenada de numeros inteiros e um numero n,
    e retorna uma mesma lista com n inserido na lista 
    de forma que ela continue ordenada;
    list,int -> list'''
    x=list.append(lista_numero,n)
    return list.sort(x)