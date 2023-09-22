def substitui(s,x,i):
    '''substituir a letra na posicao'''
    parte1 = s[0:i]
    parte2 = s[i+1:len(s)]
    retur parte1 + x + parte2