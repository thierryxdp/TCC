def substitui(s,x,i):
    '''Retorna uma string igual a s, exceto que o elemento da posição i 
    deve ser substituído pelo caractere x; string, int, int -> string.'''
    return s[:int(i):]+x+s[(int(i)+1)::]