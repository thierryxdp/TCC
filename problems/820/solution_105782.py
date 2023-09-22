def posLetra(frase, letra, n):
    '''Dada uma frase, uma letra e um número, retorna
    a posição exata dentro da frase a enésima letra indicada.
    '''
	if frase.count(letra) >= n :
        lista = list(frase)
        for i in range(n-1):
        num = int(lista.index())
        lista[num] = " "
        string = "".join(lista)
        return string.index(letra)
    return -1