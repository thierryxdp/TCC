def substitui(s,x,i):
    '''função que retorna a substituição de um caractere (x) de uma string
    (s), que está na posição (i) de entrada;
    string,string->int'''
    a=1+i
    
    return s[0:i]+x+s[a:-1]