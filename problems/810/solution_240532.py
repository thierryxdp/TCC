def inverte(frase):
    """ Função , dado uma frase, retorne a mesma frase inversa.
    str->str"""
    
    f1=frase.str.split(frase):
    f2=f1.str.join(frase)
    
   
	return f2[::-1]