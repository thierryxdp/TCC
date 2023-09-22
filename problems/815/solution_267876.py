def insere(lista_numero, n):
    '''
    Esta função recebe uma lista ordenada crescente de números inteiros e um número inteiro.
    Retorna uma lista contendo a lista fornecida incluindo o número fornecido, na posição correta.
    
    Parametros
    ----------
    lista_numero (list) : lista de ordenada crescente de números inteiros
    n (int) : número inteiro
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero