def posLetra(frase, letra, n):
    '''Retorna em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida,
    a função deve retornar -1.
    frase ->str '''
    qtd = str.count(frase,letra) #3
    if qtd < n:
        return -1
    else:
        i=0
        p=0
        while i<len(frase):
            p = str.index(frase,letras,i)
            i = p + 1
        return p