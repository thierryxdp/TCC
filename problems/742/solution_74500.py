def substitui(s,x,i):
    '''substitui a letra na posicao escolhida'''
    '''str--->str'''
    parte1=s[0:1]
    parte2=s[i+1:len(s)]
    return parte1+x+parte2