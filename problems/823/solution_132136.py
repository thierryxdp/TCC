def faltante(n_pecas):
    ''' funcao que descobre qual peça que nao se encontra no quebra cabeça
list -> int '''
    numeropecas = n_pecas [:]
    numeropecas.sort()
    contador = 0
    n_pecas = -1
    while (contador <len(numeropecas)):
        if numeropecas[contador] == (contador + 1):
            contador = contador + 1
        else:
            n_pecas = contador + 1
            contador = len(numeropecas)
    if (n_pecas == -1):
        n_pecas = len(numeropecas)+1
    return n_pecas