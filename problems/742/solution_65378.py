def substitui(s,x,i):
    '''função que recebe très variaveis e retorna o string (s)
    excero que o elemento da posição (i), porque é substituido
    por (x)
    string, int, int -> string
    '''
    return s[0:i]+x+s[i+1:]