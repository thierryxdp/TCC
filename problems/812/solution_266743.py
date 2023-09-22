def retira_pontuacao(frase):
    """."""
    caracteres = "–",",",":",".",";","?","!"
    if "–" in frase:
        frase += str.replace(frase, "–", " ")   
    if "," in frase:
        frase += str.replace(frase, ",", " ")
    if ":" in frase:
        frase += str.replace(frase, ":", " ")
    if "." in frase:
        frase += str.replace(frase, ".", " ") 
    if ";" in frase:
        frase += str.replace(frase, ";", " ")
    if "?" in frase:
        frase += str.replace(frase, "?", " ")
    if "!" in frase:
        frase += str.replace(frase, "!", " ")
  	return frase