def bolos(a,b,c):
    '''calcula o numero maximo de bolos que podem ser feitos'''
    Amin = a//2
    Bmin = b//3
    Cmin = c//5
    	return min(Amin,Bmin,Cmin)