def conta_frases(texto):
    """Retorna o número de frases de um texto dado; str -> int"""
    y = int(str.count(texto,"...")) 
    z = int(str.count(texto,"!"))
    w = int(str.count(texto,"?"))
    x = int(str.count(texto,"."))//4
    if y>0 :
        return y+z+w+x
    elif y==0
        z+w+(x*4)