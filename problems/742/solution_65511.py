def substitui(s,x,i):
    '''Retorna uma string(s), que deve ser escrita entre 'aspas' 
    com uma parte (i),entre 0 e o comprimento da string, 
    substituída por um caractere(x)
    string, string, int -> string '''
    return s[:i]+x+s[i+1:]