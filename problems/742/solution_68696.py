def substitui(s,x,i):
    '''
    	Funcao que recebe uma string(s), um caractere (x) e 
        um numero inteiro (i) entre 0 e o comprimento da 
        string, e retorna uma string igual a s
        string, int, int -> string
    '''
    return s[0:i] + str(s[i]) + s[i+1:]