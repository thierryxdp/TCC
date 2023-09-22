def remover(frase):
    a = str.replace(frase, "!", '')
    b = str.replace(a, ",", '')
    c = str.replace(b, ".", '')
    d = str.replace(c, "-", ' ')
    e = str.replace(d, ":", '')
    f = str.replace(e, ";", '')
    g = str.replace(f, "...", '')
    h = str.replace(g, "''", '')
    return h
 
def inverte(frase):
    frase2= str.lower(remover(frase))
    lista=str.split(frase2,' ')
    list.reverse(lista)
    final= str.join('',lista)
    
    return final