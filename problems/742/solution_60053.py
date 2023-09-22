def substitui(s,x,i):
    """ Substitui o caractere x na posição i da string s.
    	str, str, int -> str
        
    	Parameters:
        s: String a ser substituída.
        x: Caractere a ser inserido na string.
        i: Posição do caractere a ser substituído da string.
        
        Returns:
        Uma string igual a s, exceto que o elemento da posição i é substituído pelo caractere x.
    """  
    return s[ : i ] + x + s[ i + 1 : ]