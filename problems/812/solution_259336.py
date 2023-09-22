def verifica(caracter):
    pontuacao = ["...", ",", ";", ":", "!", "-"]
    return " " if caracter in pontuacao else caracter

def retira_pontuacao(frase):
    frase = str.join("", list(map(verifica, frase)))
    return frase