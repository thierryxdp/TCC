def inverte(frase):
    
    x=str.split(frase," ")
    x.reverse()
    x1 = ''.join(x)
    y = str.split(x1,"-")
    y1 = ''.join(y)
    z = str.split(y1,"!")
    z1 = ' '.join(z)
    return z1