def substitui(s,x,i):
    '''funcao que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento
da posicao i deve ser substituido pelo caractere x;
    string, string, int-> string'''
    
    return str(s)[0:i]+str(x)+ str(s)[i+1:]: