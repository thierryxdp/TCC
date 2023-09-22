def retira_pontuacao(frase):
    if texto in "!":
        return str.join(" ", str.split(frase,"!"))
  	if texto in "-":
        return str.join(" ", str.split(frase,"-"))
   	if texto in ",":
        return str.join(" ", str.split(frase,","))
   	if texto in ":":
        return str.join(" ", str.split(frase,":"))
   	if texto in ";":
        return str.join(" ", str.split(frase,";"))
  	if texto in ".":
        return str.join(" ", str.split(frase,"."))
  	if texto in "!":
        return str.join(" ", str.split(frase,"?"))