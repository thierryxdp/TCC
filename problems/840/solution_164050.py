def bolos(A,B,C):
    """
    	Determina qual a quantidade maxima de bolos 
        que podem ser feitos
        
        Parametros: 
        		A,B,C: int.
        		Valores das quantidades de farinha, ovo e leite
        Returns: 
        		int
                Um numero representando a quantidade maxima de bolos
    """
    a = round(A/2+0.5)
    b = round(B/3+0.5)
    c = round(C/5+0.5)
    
    return min(a,b,c)