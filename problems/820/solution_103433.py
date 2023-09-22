def posLetra(string,letra,n):
	''' Essa função tem como objetivo contar quantas letras tem em uma
    string, dado um número de vezes que ele quer que ocorra, caso não
	aconteça, a resolução volta (-1).
	str,str,int -> int'''

    s = str.count(string,letra)
    i=-1
    
    if  s < n:
        return i
    else:
     
    	while i <= len(string):
        	i = i+1
		    if letra in string[i]:
            	posicao = i
    			return posicao