def substitui(s,x,i):
     '''dados uma string (s), um caractere (x) e um numero inteiro (i) entre 0 e o comprimento da string, calcula e retorna uma string igual a 
    s, exceto que o elemento da posiçao i deve ser substituido pelo caractere x
       : str, str, int -> str
    '''
        if (0<=i<=len(s)):
            s= ((s[0:i]) + (str(x)) + (s[i+1:]))
            return s