def retira_pontuacao(frase):
    """ Essa função retira a pontuação da frase introduzida e retorna-a. str->str"""
    if ","  in frase:
        frase = frase.replace("," , " ")
    if "!"  in frase:
        frase = frase.replace("!" , " ")
    if "?"  in frase:
        frase = frase.replace("?" , " ")
    if "-"  in frase:
        frase = frase.replace("-" , " ")
    if "."  in frase:
        frase = frase.replace("." , " ")
    return frase

def inverte(frase):
    """ Essa função retorna a frase incluida na ordem inversa das palavras, sem letras maiúsculas e sem pontuação"""
    frase = str.lower(retira_pontuacao(frase))
    return frase