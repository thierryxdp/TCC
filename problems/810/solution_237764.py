def inverte(frase):
    

    y = str.replace(frase,"-"," ")
    y1 = str.replace(y,".","")
    y2 = str.replace(y1,"!","")
    
    z = str.split(y1,"!")
    z1 = ''.join(z)
    
    x=str.split(z1," ")
    x.reverse()
    x1 = ' '.join(x)
    return str.lower(x1)