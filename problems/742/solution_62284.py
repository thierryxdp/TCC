def substitui(s,x,i):
    '''modifica a str (s), dado um caractere (x), e o número (i) que indica 
a posição na str o caractere a ser substituido; str,str,int->str'''
    n_carac=len(s)
    return s[0:i]+x+s[i+1:n_carac]