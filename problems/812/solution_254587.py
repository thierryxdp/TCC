def retira_pontuacao(frase):
    if "!" in frase:
        frase=str.join(" ", str.split(frase,"!"))
  	if "-" in frase:
   		frase=str.join(" ", str.split(frase,"-"))
   	if "," in frase:
		frase=str.join(" ", str.split(frase,","))
   	if ":" in frase:
   		frase=str.join(" ", str.split(frase,":"))
   	if ";" in frase:
   		frase=str.join(" ", str.split(frase,";"))
  	if "." in frase:
 		frase=str.join(" ", str.split(frase,"."))
  	if "!" in frase:
   		frase=str.join(" ", str.split(frase,"?"))
    return frase