def inverte(frase):
    """ Função , dado uma frase, retorne a mesma frase inversa.
    str->str"""
    
    f1=frase.str.split(frase,2)
    f2=f1.str.join(2,frase)
   
	return frase[::-1]