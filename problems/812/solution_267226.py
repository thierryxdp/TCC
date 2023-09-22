def retira_pontuacao(frase):
    texto=frase.replace(",")
    texto=frase.replace(":")
    texto=frase.replace(";")
    texto=frase.replace(".")
    return texto.split(" ")