def faltante(lista):
    '''Função que retorna o número da peça
    faltante.
    Dados de entrada: list
    Valor de saída: int
    '''
    lista_pecas = lista[:]
    x = 0 #Numero inteiro que nao pertence a lista 
    i = 1
    while i < len(lista_pecas):
        if i in lista_pecas:
            i = i + 1
        if i not in lista_pecas:
            lista_pecas.append(i)
            lista_pecas.sort()
            x = i 
    return x