def retira_pontuacao(frase):
    if "-" in frase:
        a=str.split(frase,"-")
        return a
    if "," in frase:
        a=str.split(frase,",")
        return a
    if ":" in frase:
        a=str.split(frase,":")
        return a
    if ";" in frase:
        a=str.split(frase,";")
        return a
    if "?" in frase:
        a=str.split(frase,"?")
        return a
    if "!" in frase:
        a=str.split(frase,"!")
        return a
    if "." in frase:
        a=str.split(frase,".")
        return a