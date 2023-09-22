def substitui(s,x,i):
    '''retorna a string s porém substituindo o elemento da posição i pelo caractere x;
    string, int, int -> string'''
    comeco=s[0:i]
    fim=s[i+1:]
    return comeco + str(x) + fim