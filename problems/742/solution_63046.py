def substitui(s,x,i):
    '''Retorna uma string com o elemento da posicao i substituido por x
    	sendo 0<i<Comprimento da string
    	entrada-> str, str, int
        Retorna-> str'''
    return s.replace(s[i:],x)