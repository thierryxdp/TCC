def inverte(frase):
    

    y = str.replace(frase,"-"," ")
    y1 = str.replace(y,".","")
    y2 = str.replace(y1,"!","")
    
    z = str.split(y1,"!")
    z1 = ''.join(z)
    return str.lower(z1)