def substitui(s,x,i):
    #s = string
    #x = letra
    #i = posição
    nova_frase = s
    termo_antigo = s[i]
    if i < len(s) and i >= 0:
        nova_frase = str.replace(s,termo_antigo,i)
    return nova_frase