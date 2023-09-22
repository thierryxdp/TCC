def substitui(s,x,i):
    '''Função que dada uma string 's' um carectere 'x' e numero inteiro 'i', irá fazer uma substituição por x na posição i. 
    str, str, int -> str '''
    return s[:i]+x+s[i+1::]