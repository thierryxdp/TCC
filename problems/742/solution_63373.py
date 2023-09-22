def substitui(s,x,i):
    """funcao que recebe uma string s, um caractere x e um inteiro i entre 0 e o comprimento da string e retorna a string s modificada pela substituicao do elemento da posicao i pelo cacatere x;
       string, string, int -> string"""
    if i==0:
        return x+s[1:len(s)]
    elif 0<i< len(s):
        return s[0:i]+x+s[i+1:len(s)]
    elif i==len(s): 
        return s[0:(len(s)-1)]+x