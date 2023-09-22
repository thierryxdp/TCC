def substitui(s,x,i):
    """ 0<=i<=comprimento da string. Recebe uma string s, um caractere x  e um número inteiro i entre - e o comprimento da string e retorna uma string igual s, mas com o elemento da posição i substituído pelo caractere x"""
    a=int(i)
    b=int(i+1)
    c=int(len(s))
    d=str(s[0:a])
    e=str(s[b:c])
    return d +str(x) + e