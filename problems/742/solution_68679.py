def substitui(s,x,i):
    '''
    	Funcao que recebe uma string(s), um caractere (x) e 
        um numero inteiro (i) entre 0 e o comprimento da 
        string, e retorna uma string igual a s
        string, int, int -> string
    '''
    x = s[i]
    final = s[0;i] + x + s[i+1;]
    return final