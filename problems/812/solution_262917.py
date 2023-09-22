def retira_pontuacao(frase):
    """Essa funcao recebe uma frase como entrada e retorna a mesma substituindo os carecteres de pontuacao, por espacos
    str->str"""
    frase = str.strip(frase, "-",",",":",";",".","?","!")
    frase = str.join(" ", frase)
    return frase