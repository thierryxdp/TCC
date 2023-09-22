def substitui(s,x,i):
    ''' dada uma a string s, retorna uma string similiar a s, porém a posição
    i (dada) da string será substituída pelo caractere x string, int, int -> string '''
    return s[:i]+str(x)+s[i+1:]