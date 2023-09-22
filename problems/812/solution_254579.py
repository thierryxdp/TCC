def retira_pontuacao(frase):
    if "!" in texto:
        frase=str.join(" ", str.split(frase,"!"))
  	if "-" in texto:
   		frase=str.join(" ", str.split(frase,"-"))
   	if "," in texto:
		frase=str.join(" ", str.split(frase,","))
   	if ":" in texto:
        frase=str.join(" ", str.split(frase,":"))
   	if ";" in texto:
        frase=str.join(" ", str.split(frase,";"))
  	if "." in texto:
        frase=str.join(" ", str.split(frase,"."))
  	if "!" in texto:
        frase=str.join(" ", str.split(frase,"?"))
    return frase