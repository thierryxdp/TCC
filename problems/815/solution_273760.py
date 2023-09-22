def insere(lista_numero,n):
    ''' funcao que recebe uma lista com numeros
        e um numero inteiro 'n' e retorna uma nova lista 
        com o 'n' incluido nela de maneira ordenada, atraves
        das funcoes 'append' e 'sort'.
        list, int -> list'''
    x= lista_numero
    x.append(n)
    x.sort()
    return x