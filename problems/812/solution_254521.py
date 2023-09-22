def retira_pontuacao(frase):
    """Essa funcao recebe 'frase' str -> str
substitui as pontuacoes utilizando a funcao replace
de str"""
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, ".", " ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    frase = str.replace(frase, "...", " ")
    return frase