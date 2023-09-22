def inverte(frase):
    x = str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' ',),',',' ',),'-',' ',),':',' ',),';',' ',),'!',' ',),'?',' ',))
    y = str.split(x)
    return y[::-1]