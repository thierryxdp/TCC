def retira_pontuacao(texto):
    '''dada uma frase retorna a frase onde os caracteres de pontuação de encerramento de frase tenham sido substituido por espaço
    string -> string'''
    frase = str.replace(texto, "-", " ")
    frase = str.replace(texto, ",", " ")
    frase = str.replace(texto, "...", " ")
    frase = str.replace(texto, "..", " ")
    frase = str.replace(texto, ".", " ")
    frase = str.replace(texto, ";", " ")
    frase = str.replace(texto, "!", " ")
    frase = str.replace(texto, "?", " ")
    return frase