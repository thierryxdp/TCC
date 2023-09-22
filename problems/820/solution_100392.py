def posLetra(texto,letra,num):
    '''Dados um texto, uma letra e um número (1 para
    primeira ocorrência, 2 para segunda...), retorna a 
    posição da string em que a ocorrência da letra está,
    caso exista menos ocorrências da letra do que a
    ocorrência pedida, a função retornará -1.
    str, str, int -> int'''
    ocorrencia = 0
    inicio = str.index(texto,letra)
    while ocorrencia < num:
        if letra in texto:
            str.index(texto,letra,inicio)
        else:
            return -1
    	ocorrencia = ocorrencia + 1
        inicio = inicio + str.index(texto,letra)
    return str.index(texto,letra)