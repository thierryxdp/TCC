def retira_pontuacao(frase):
    """."""
    caracteres = frase
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
  	return caracteres