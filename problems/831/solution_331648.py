def lingua_p(palavra):
    ''' Essa função tem como objetivo retornar a palavra dada em linguagem
    do P.'''
    '''str->str'''
    palavra1 = str.lower(palavra)
    i=0
    linguap = ''
    while i < len(palavra1):
        if palavra1[i] not in 'bcdfghjklmnpqrstvwxyzç':
        linguap = palavra1[i]
        	linguap += palavra1[i]+'p'+palavra1[i]
		i+=1
	
    return linguap