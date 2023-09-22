def uppCons (frase):
    '''função que recebe como entrada uma frase e retorna com
    todas as suas consoantes maiúsculas e as demais letras
    como estavam'''
    s = ''
    n = 0
    	while n < len(frase):
        	if frase [n] in 'bcdfghjklmnpqrstvwxyzç':
            	s = s + str.upper(frase [n])
        	else:
            	s = s + str(frase [n])
        	n = n + 1
    	return s