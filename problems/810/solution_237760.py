def inverte(frase):
    
    x=str.split(frase," ")
    x.reverse()
    x1 = ' '.join(x)
    y = str.replace(x1,"-"," ")
    y1 = str.replace(y,".","")
    y2 = str.replace(y1,"!","")
    
    z = str.split(y1,"!")
    z1 = ''.join(z)
    return z1