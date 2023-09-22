def substitui(s,x,i):
    #s = string
    #x = letra
    #i = posição
    if i < len(s) and i >= 0:
        nova_frase = str.replace(s,s[i],x)
        return nova_frase
    else:
        return s