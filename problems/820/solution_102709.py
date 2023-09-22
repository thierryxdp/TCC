def posLetra(frase,letra,num):
    
    if num < str.count(frase,letra):
        return -1
    else:
    	return str.index(str.replace(frase,letra,' ', (num -1)),letra)