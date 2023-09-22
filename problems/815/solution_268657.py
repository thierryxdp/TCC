def insere(lista_numero,n):
    '''Retorna uma lista com os inteiros
       em ordem crescente e com n na posição
       correta;list,int->list'''
    numeros=lista_numero+[n]
    list.sort(numeros)
    return numeros