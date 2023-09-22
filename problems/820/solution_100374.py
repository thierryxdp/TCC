def posLetra(texto,letra,num):
    '''Dados um texto, uma letra e um número (1 para
    primeira ocorrência, 2 para segunda...), retorna a 
    posição da string em que a ocorrência da letra está,
    caso exista menos ocorrências da letra do que a
    ocorrência pedida, a função retornará -1.
    str, str, int -> int'''
    ocorrencia = 0
    while ocorrencia < num:
        if letra in texto:
            str.index(texto,letra)
        else:
            return -1
    	ocorrencia = ocorrencia + 1    
    return str.index(texto,letra,ocorrencia)