def conta_frases(frase):
    
    ret = 0
    x = str.index(frase, ".")
    if "." in frase and frase[x] == frase[x+1]:
        ret = 3
    
    return str.count(frase,".") + str.count(frase,"!") + str.count(frase,"?") - ret