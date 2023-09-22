def retira_pontuacao(frase):
    if "." in frase:
        frase2=str.replace(frase,".", " ")
        return frase2
    elif "," in frase2:
        frase3=str.replace(frase,",", " ")
        return frase3
    elif "-" in frase3:
        frase4= str.replace(frase,"-", " ")
        return frase4
    elif ";" in frase4:
        frase5=str.replace(frase,";", " ")
        return frase5
    elif ":" in frase5:
        frase6=str.replace(frase,":", " ")
        return frase6
    elif "!" in frase6:
        frase7=str.replace(frase,"!", " ")
        return frase7
    elif "?" in frase7:
        frase8=str.replace(frase,"?", " ")
        return frase8