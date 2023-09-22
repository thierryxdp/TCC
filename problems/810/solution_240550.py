def inverte(frase):
    """ Função que, dado uma frase, retorne a mesma frase inversa.
    str->str"""
    
    f1 = frase.str.split(" ",-1)
    f2 = f1.str.join(-1," ")
    
   
	return f2[::-1]