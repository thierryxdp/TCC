def substitui(s,x,i):
    '''função que retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x;
       str, str, int -> str'''
    return s[0:i]+ x+ s[i+1:len(s)]