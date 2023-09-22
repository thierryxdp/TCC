def substitui(s,x,i):
    ''' retorna uma string igual a s, exceto que o elemento da posição i deve substituir o x;
    str, int, int->str '''
    return s[0:i]+x+s[i+1:len(s)]