def posLetra(string,letra,num):
    '''Função que recebe uma string, uma letra, e um número e 
    retorna em que posição aquela ocorrência da letra está.
    str,str,int->int
    '''
    i=0
    ocorrencia=0
    while i<len(string):
        if string[i] == letra:
            ocorrencia+=1
        if ocorrencia==num:
        	return i
        i+=1
    return -1