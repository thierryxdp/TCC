def substitui(s,x,i):
    '''funcao que substitui o elemento da posicao i da string pelo carcater x, sendo i um
    inteiro positivo menor que o comprmento da string; string, int, int -> string'''
    return s[0:i] + str(x) + s[i:]