def retira_pontuacao(frase):
    frase1 = str.replace(frase, '.',' ')
    frase2 = str.replace(frase, '!'' ')
    if '!' in frase == True:
        return frase2
    else:
        return frase1