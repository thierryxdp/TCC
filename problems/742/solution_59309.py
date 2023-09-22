def substitui(s,x,i):
    '''função que recebe uma string, um caractere e um inteiro (de 0 a len(s)
    e retorna uma string parecida com a original, exceto pelo fato de na posição i,
    o caractere original ser substituído pelo caractere x indicado. 
    str, int, int -> str'''
    return s[0:i]+str(x)+s[(i+1):]