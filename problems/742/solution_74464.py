def substitui(s,x,i):
    '''mudar a letra na posicao escolhida e colocar a palavra nas aspas. str ---> str'''
    parte1 = s[0:i]
    parte2 = s[i+1:len(s)]
    return parte1 + x + parte2