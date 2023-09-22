#a funcao retorna a frase substituindo seus pontos por espaca
def retira_pontuacao(x):
    if "-" in x:
        x = str.replace(x, "-", " ")
    if "," in x:
        x = str.replace(x, ",", " ")
    if ":" in x:
        x = str.replace(x, ":", " ")
    if ";" in x:
        x = str.replace(x, ";", " ")
    if "." in x:
        x = str.replace(x, ".", " ")
    if "?" in x:
        x = str.replace(x, "?", " ")
    if "!" in x:
        x = str.replace(x, "!", " ")
    return x