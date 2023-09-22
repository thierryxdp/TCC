def retira_pontuacao(texto):
    "função que dado uma frase, retorne a frase onde todos os caracters de pontuação tenham sido substituidas por espaço"
    texto = texto.replace("-", " ")
    texto = texto.replace(",", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace(".", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")
    return texto