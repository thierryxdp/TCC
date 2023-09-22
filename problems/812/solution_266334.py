def retira_pontuacao(frase):
    frase= str.replace(frase,"-"," ")
    frase= str.replace(frase,","," ")
    frase= str.replace(frase,":"," ")
    frase= str.replace(frase,";"," ")
    frase= str.replace(frase,"."," ")
    frase= str.replace(frase,"..."," ")
    frase= str.replace(frase,"!"," ")
    frase= str.replace(frase,"?"," ")
    if ("  " in frase) and (frase[0]==" ") and (frase[-1]==" "):
        frase= str.replace(frase,"  "," ")
        frase= frase[1:-1]
        return frase
    elif ("  " in frase) and (frase[0]==" "):
        frase= str.replace(frase,"  "," ")
        frase= frase[1:]
        return frase
    elif ("  " in frase) and (frase[-1]==" "):
        frase= str.replace(frase,"  "," ")
        frase= frase[:-1]
        return frase
    elif (frase[0]==" ") and (frase[-1]==" "):
        frase= frase[1:-1]
        return frase
    elif "  " in frase:
        frase= str.replace(frase,"  "," ")
        return frase
    elif frase[0]==" ":
        frase= frase[1:]
        return frase
    elif frase[-1]==" ":
        frase= str.replace(frase,"  "," ")
        frase= frase[:-1]
        return frase
    else:
        return frase