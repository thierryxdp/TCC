def insere(lista_numero, n):
    '''
    Ao inserir a lista de números inteiros crescentes e um número inteiro, 
    o código irá encaixar o número inteiro na posição correta na lista inserida.
    list -> list
    '''
    list.insert(lista_numero, 0, n)
    list.sort(lista_numero)
    return lista_numero