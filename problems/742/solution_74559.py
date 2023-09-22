def substitui(s,x,i):
    #s = string
    #x = letra
    #i = posição
    nova_frase = s
    if i < len(s) and i >= 0:
        nova_frase = str.replace(s,s[i],x)
    return nova_frase