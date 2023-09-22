def conta_frases(texto):
    """"Esta é a função que dada um texto retorna quantas frases ele possui, str -> int"""
    texto1= str.replace(texto,"!",".")
    texto2= str.replace(texto1,"?",".")
    texto3= str.replace(texto2,"...",".")
    x= str.split(texto3,".")
    y= len(x)
    z= y-1
    return z