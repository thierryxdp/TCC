def substitui(s,x,i):
    ''' funcao que receba uma string s, um caractere x e um
numero inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento
da posicao i deve ser substituido pelo caractere x;
str , str , int -> str '''
    return s[0:i] + x + s[i+1:len(s)]