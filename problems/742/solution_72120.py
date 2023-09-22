def substitui(s,x,i):
    '''função que substitui o caracter x inserido na posição i da string
    s, começando a contagem a partir do 0; deve-se inserir s,x,i respecti-
    vamente
    string,int,int->string'''
    return s[0:i]+x+s[(i+1):]