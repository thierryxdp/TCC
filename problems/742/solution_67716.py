def substitui(s,x,i):
    'dados uma strig,um caractere e um inteiro retorne a string contendo x na posição i'
    return s[0:i] + x + s[i+1: ]