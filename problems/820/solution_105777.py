def posLetra(frase, letra, n):
    '''Dada uma frase, uma letra e um número, retorna
    a posição exata dentro da frase a enésima letra indicada.
    '''
    def posLetra(frase, letra, n):
    contador = 0
    while str.find(frase, letra) != -1:
        frase = str.partition(frase, letra)[2]
        contador = contador + 1
    if contador > n:
        return n
    if contador <= n:
        return contador
    else:
        return -1