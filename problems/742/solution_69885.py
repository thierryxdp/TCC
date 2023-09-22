def substitui(s,x,i):
    '''
    	Funçao que recebe uma string, um caractere e um numero inteiro
        e retorna a string com o caractere x na posiçao do numero inteiro
        string, int, int -> string
    '''
    
    return s[0:i] + x + s[i+1:]