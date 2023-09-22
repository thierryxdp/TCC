def posLetra(string,letra,n):
    ''' Essa função tem como objetivo contar quantas letras tem em uma
    stringer, dado um número de vezes que ele quer que ocorra, caso não
    aconteça, a resolução volta (-1).
    str,str,int -> int'''
    

    s = str.count(letra,string)
    i=0
    
    if  s < n:
        return -1
    else:
        
    	while i <= len(string):
        	if string[1] in letra:
            posicao = i
            i = n
            return n