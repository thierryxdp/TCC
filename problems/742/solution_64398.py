def substitui(s,x,i):
    """ Recebe uma string s, um caractere x  e um número inteiro i entre - e o comprimento da string e retorna uma string igual s, mas com o elemento da posição i substituído pelo caractere x"""
    a=int(i-1)
    b=int(i+1)
    c=int(len(s))
    return str(s[0:a])+'x'+ str(s[b:c])