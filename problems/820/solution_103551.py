def posLetra(frase, letra, n):
    '''Retorna em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida,
    a função deve retornar -1.
    frase ->str '''
    qtd = str.count(frase,letra)
    if qtd < n:
        return -1
    else:
        i+=1
        p=0
        while i<n:
            p = str.index(frase,letra,i)       
        return n