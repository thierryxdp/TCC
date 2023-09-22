def substitui(s,x,i):
    '''Função que irá receber uma string s, um caractere x e
    um número inteiro i (de 0 a o comprimento da string), 
    retornanto a string s, só que substituindo a letra da 
    posição i da string s, pelo caractere x;
    string, string, int -> string'''
    c = len(s)
    s2=(s[0:i]+x+s[(i+1):c])
    return (s2)