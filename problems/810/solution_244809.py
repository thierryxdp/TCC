def inverte(frase):
    x=str.replace(frase,'.',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,'-',' ')
    w=str.replace(z,'!',' ')
    xx=str.replace(w,'?',' ')
    return str.split(xx)