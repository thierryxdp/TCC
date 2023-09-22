def posLetra(texto,letra,num):
    '''Dados um texto, uma letra e um número (1 para
    primeira ocorrência, 2 para segunda...), retorna a 
    posição da string em que a ocorrência da letra está,
    caso exista menos ocorrências da letra do que a
    ocorrência pedida, a função retornará -1.
    str, str, int -> int'''
    ocorrencia = 0
    resposta = []
    if str.count(texto,letra)>num:
        while ocorrencia < num:
            resposta = resposta + [str.index(texto,letra,ocorrencia)]
            ocorrencia = ocorrencia + str.index(texto,letra,ocorrencia)
        	return resposta[-1]    
    else:
    	return -1