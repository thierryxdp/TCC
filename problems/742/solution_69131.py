def substitui(s,x,i):
    ''' Funçao que recebe uma string s, um caractere x e um numero
    inteiro i entre 0 e o comprimento da string, e retorna uma string
    igual a s, exceto que o elemento da posiçao i deve ser substituido
    pelo caractere x.
    str, int, int -> str
    '''
    if i==0:
        return x+s[1:]
    if i==[len(s)]:
        return s[len(s)] + x
    if i==i>0:
        return s[0:i]+ x + s[i+1:]