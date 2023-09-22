def posLetra(frase,letra,num):
    '''
	'''
	i=1
    result=''
    while (i<=num):
        a = frase.find(letra)
        if i ==num:
            result = frase[a:].find
        i+=1
    return result