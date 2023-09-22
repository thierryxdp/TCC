def uppCons(frase):
    """função que retorna a frase inserida com consoantes maiusculas
str->str"""
    newfrase=[]
    n=0
    while n<len(frase):
        if frase[n] in 'BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz':
        	list.append(newfrase,str.upper(frase[n]))
            n=n+1
        else:
            list.append(newfrase,frase[n])
            n=n+1
    return str.join('',newfrase)