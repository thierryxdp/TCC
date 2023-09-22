def insere(lista_numero,n):
    '''Função que recebe uma lista e um número inteiro, e esse número
    tem que entrar na lista sem alterar a sua ordenação.
    tipo de entrada: list e int
    tipo de saída: list'''
    lista_numero.append(n)
    return list.sort(lista_numero)