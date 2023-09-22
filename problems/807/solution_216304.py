def conta_frases(frase):
    
    ret = 0
    x = str.index(frase, ".")
    if frase[x] == frase[x+1]:
        ret = 3
    
    return str.count(frase,".") + str.count(frase,"!") + str.count(frase,"?") - ret