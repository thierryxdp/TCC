def inverte(frase):
    
    x=str.split(frase,"!")
    y=str.split(x,",")
    x.reverse()
    
    return ' '.join(x)