def substitui(s,x,i):
    '''recebe uma string s e um caracter x que será sigstituido na posição i'''
    novo_s = s[:i] + x + s[i+1:]
    return novo_s