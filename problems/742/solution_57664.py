def substitui(s,x,i):
    '''retorna a string s com o elemento da posição i substituido pelo caractere x;
    str, str, int -> str'''
    return s[:i]+str(x)+s[i+1:]