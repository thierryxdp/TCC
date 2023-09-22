def inverte(frase):
    """ Função que, dado uma frase, retorne a mesma frase inversa.
    str->str"""
    
    f1 = frase.str.split()
    f2 = f1.str.join()
  
	return f2[::-1]