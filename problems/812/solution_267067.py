def retira_pontuacao (frase):
    '''Recebe uma frase e retorna a mesma sem pontuação, tendo um espaço 
    no lugar desta (str -> str)(pontuação:'-',',',':',';','.','?'e'!')'''
    if "-" in frase:
        frase1 = frase.replace("-"," ")
    else:
        frase1 = frase
    if "," in frase:
        frase2 = frase1.replace(","," ")
    else:
        frase2 = frase1
    if ":" in frase:
        frase3 = frase2.replace(":"," ")
    else:
        frase3 = frase2
    if ";" in frase:
        frase4 = frase3.replace(";"," ")
    else:
        frase4 = frase3
    if "." in frase:
        frase5 = frase4.replace("."," ")
    else:
        frase5 = frase4 
    if "?" in frase:
        frase6 = frase5.replace("?"," ")
    else:
        frase6 = frase5
    if "!" in frase:
        frase7 = frase6.replace("!"," ")
    else:
        frase7 = frase6
        return frase7