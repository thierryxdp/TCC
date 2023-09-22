def inverte(texto):
    '''dada uma frase retorne outra frase com as palavras na ordem inversa sem letras maiúsculas e sem pontuação
    string -> string'''
    frase = str.replace(texto, "-", " ")
    frase1 = str.replace(frase, ",", " ")
    frase2 = str.replace(frase1, "...", " ")
    frase3 = str.replace(frase2, "..", " ")
    frase4 = str.replace(frase3, ".", " ")
    frase5 = str.replace(frase4, ";", " ")
    frase6 = str.replace(frase5, "!", " ")
    frase7 = str.replace(frase6, "?", " ")
    frase_minuscula = str.lower(frase6)
    frase_nova str.join("-1", texto)