def posLetra(s, letra, n):
    
    """Retorna o indice da nesima vez q a letra aparece na string dada de entrada, caso nao apareca na nesima vez 
    retorna -1"""
    
    i=0
    c=0
    while i < len(s):
        if s[i] == letra:
            c = c + 1
            if c == n:
                return i
    	i = i + 1
   	    return -1