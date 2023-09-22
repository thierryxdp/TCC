def insere(lista_numero,n):
    '''Escreva uma lista de numeros entre [] e um numero qualquer.
    A funcao retorna o numero dentro da lista, com todos os seus 
    elementos ordenados, ou seja, do menor para o maior.
    list, int -> list'''
    lista_numero.append(n) #adiciona n a lista
    return lista_numero.sort()