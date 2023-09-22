def substitui(s,x,i):
    '''substituir a letra na posição escolhida.
    str--> str'''
    pt1 = s[0:i]
    pt2 = s[i+1:len(s)]
    return pt1 + x + pt2