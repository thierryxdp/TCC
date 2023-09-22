def substitui(s,x,i):
    '''funcao que substitui o elemento da posicao i pelo caractere x na string s; str int, int -> str'''
    return s[0:i] + x + s[i+1:]