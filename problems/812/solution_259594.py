def retirar_pontuacao(frase):
    frase = str.split(frase, ",", ".", ":","/", "-")
    frase = str.join(" ", frase)
   return frase