def substitui(s,x,i):
    dadas as entradas s, x, i a funçao retorna uma string s 
    com um caractere x na posiçao i;  string, int, int -> string
    a=int(i)+1
    return s[0:i]+ x +s[a:]