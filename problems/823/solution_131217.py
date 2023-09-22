def faltante(lista):
    '''Função que retorna o número da peça
    faltante.
    Dados de entrada: list
    Valor de saída: int
    '''
    lista.sort()
    pecas = len(lista) + 1 
    x = 0 #Numero inteiro que nao pertence a lista 
    i = 1 #Contador
    while i < pecas:
        if i not in lista:
            x = i  
            return x
        if i + 1 not in lista:
            x = i + 1
        i = i + 1
    return x