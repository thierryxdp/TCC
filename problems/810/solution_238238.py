def retira_pontuacao(frase):
    """ Essa função retira a pontuação da frase introduzida e retorna-a. str->str"""
    if ","  in frase:
        frase = frase.replace("," , "")
    if "!"  in frase:
        frase = frase.replace("!" , "")
    if "?"  in frase:
        frase = frase.replace("?" , "")
    if "-"  in frase:
        frase = frase.replace("-" , "")
    if "."  in frase:
        frase = frase.replace("." , "")
    return frase

def inverte(frase):
    """ Essa função retorna a frase incluida na ordem inversa das palavras, sem letras maiúsculas e sem pontuação"""
    frase = str.lower(retira_pontuacao(frase))
    frase2 = str.split(frase)
    frase3 = frase2[-1:-(len(frase2)+1):-1]
    frase4 = str.join(" ", frase3)
    return frase2