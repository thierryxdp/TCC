def substitui(s,x,i):
    '''
    função recebe uma string s, um 
    caracetere x e um inteiro i entre 0 e o 
    comprimento da string, e retorna uma str 
    igual a s. 
    '''
    return s[:i] + x + s[i+1:]