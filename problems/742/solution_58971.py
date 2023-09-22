def substitui (s,x,i):
    '''dada uma str s, substitui o caractere de número i pelo caractere desejado x'''
    a=i
    b=i+1
    return s[0:a]+x+s[b:]