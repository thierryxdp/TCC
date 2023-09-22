def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i]=="b" or frase[i]=="c" or frase[i]=="d" or frase[i]=="f" or frase[i]=="g" or frase[i]=="h" or frase[i]=="j" or frase[i]=="k" or frase[i]=="l" or frase[i]=="m" or frase[i]=="n" or frase[i]=="p" or frase[i]=="q" or frase[i]=="r" or frase[i]=="s" or frase[i]=="t" or frase[i]=="v" or frase[i]=="x" or frase[i]=="y" or frase[i]=="w" or frase[i]=="z":
            frase[i] == str.upper(frase[i])
            
        i = i+1
            

    return frase