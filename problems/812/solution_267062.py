def retira_pontuacao (frase):
    '''Recebe uma frase e retorna a mesma sem pontuação, tendo espaço 
    no lugar desta (str -> str)(pontuação:'-',',',':',';' e '.''''
    if "-" in frase:
        frase_nova = frase.replace("-"," ")
    if "," in frase:
        frase_nova = frase.replace(","," ")
    if ":" in frase:
        frase_nova = frase.replace(":"," ")
    if ";" in frase:
        frase_nova = frase.replace(";"," ")
    if "." in frase:
        frase_nova = frase.replace("."," ")
    return frase_nova