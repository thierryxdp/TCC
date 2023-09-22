def uppCons(frase):
    '''Função que recebe uma frase e a retorna com todas as consoantes maiúsculas.
    	str -> str'''
    posicao=0
    frasefinal=frase
    while posicao<len(frase):
        if str.lower(frasefinal[posicao]) in 'bcdfghjklmnpqrstvwxyzç':
            frasefinal=str.replace(frasefinal,frasefinal[posicao],str.upper(frasefinal[posicao]))
        posicao=posicao+1
    return frasefinal