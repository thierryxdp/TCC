def quant_palavras(frase):
    i=0
    con=0
    while i<len(frase):
        if(frase[i] in " .,!?"):
            i=i+1
        else:
            i=i+1
            con=con+1
     return con