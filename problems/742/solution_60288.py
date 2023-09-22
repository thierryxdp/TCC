def substitui(s,x,i):
    '''Funcao que recebe uma string s, um caractere x
    e um numero inteiro i entre 0 e o comprimento da string,
    e retorna uma string s com o caractere x substituido na
    posicao i.'''
    s=str(s)
    x=str(x)
    metade1=s[:i]
    metade2=s[i+1:len(s)]

    return metade1+x+metade2