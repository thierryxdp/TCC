def substitui(s,x,i):
    '''funçao que recebe uma string s, caractere x e inteiro i 
    entre 0 e o comprimento da string, retorna uma string s e o
    elemento da posição i deve ser substituido pelo caractere x'''
    return s[0:i]+x+s[i+1:len(s)]