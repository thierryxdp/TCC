def inverte (frase):
    " funcao que inverte uma funcao e retira toda pontuacao"
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("-", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.lower()
    separa = frase.split()
    separa.reverse()
    return " ".join(separa)