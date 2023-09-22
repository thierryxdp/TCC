def posLetra(frase,letra,num):
    '''
    	Função que retorna a posição da string naquela ocorrência de onde a letra está.
        str, str, int -> int
	'''
	i=1
    
    a=0
    while (i<=num):
        a = frase[a:].find(letra)
        if i ==num:
            result = frase[a:].find
        i+=1
    return result