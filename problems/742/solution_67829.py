def substitui(s,x,i):
    '''
    Recebe uma palavra s, uma letra x e um número i.
    Pega a posição (i) da letra que eu quero substituir.
    Quebra a palavra em antes e depois da posição i.
    Concatena o que está antes de i e depois de i.
    Retorna o resultado. 
    str, str, int -> str
    '''
    w = s[0:i]
    y = s[i+1:len(s)]
    return w+x+y