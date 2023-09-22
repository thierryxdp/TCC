def retira_pontuacao(frase):
    if "!" in frase:
        return str.strip(frase,"!")
    elif "." in frase:
        return str.strip(frase,".")
    elif ":" in frase:
        return str.strip(frase,":")
    elif "," in frase:
        return str.strip(frase,",")
    elif "?" in frase:
        return str.strip(frase,"?")
    #elif "," and "?" in frase:
     #   return str.replace(frase,",",?",'')