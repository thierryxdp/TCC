def retira_pontuacao(texto):
    '''dada uma frase retorna a frase onde os caracteres de pontuação de encerramento de frase tenham sido substituido por espaço
    string -> string'''
    frase = str.replace(texto, "-", " ")
    frase1 = str.replace(frase, ",", " ")
    frase2 = str.replace(frase1, "...", " ")
    frase3 = str.replace(frase2, "..", " ")
    frase4 = str.replace(frase3, ".", " ")
    frase5 = str.replace(frase4, ";", " ")
    frase6 = str.replace(frase5, "!", " ")
    frase7 = str.replace(frase6, "?", " ")
    return frase