def retira_pontuacao(frase):
    """Dada uma frase retorne a frase onde todos os seus caracteres tinham sido substituidos por espaco
    string -> string """
    frase1 = str.replace(frase,  "-", " ")
    frase2 = str.replace(frase1, ".", " ")
    frase3 = str.replace(frase2, "...", " ")
    frase4 = str.replace(frase3, "..", " ")
    frase5 = str.replace(frase4, ";", " ")
    frase6 = str.replace(frase5, "?", " ")
    frase7 = str.replace(frase6, "!", " ")
    frase8 = str.replace(frase7, ",",  " ")
    frase  = str.lower(frase1)
    frase  = str.split(frase, " ")
    string = str.join(" ", frase)
    return string