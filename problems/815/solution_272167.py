def insere(lista_numero,n):
    '''Funcao que, dada uma lista ordenada de numeros inteiros (lista_numero) e um numero inteiro n, retorna a lista com n no lugar correto; list(float) -> list(float)'''
    lista_numero=lista_numero+str(n)
    return list.sort(lista_numero)