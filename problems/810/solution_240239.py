def retira_pontuacao(frase):
    
    frase = str.replace(frase, "-", " ")
    frase = str.replace(frase, ",", " ")
    frase = str.replace(frase, ":", " ")
    frase = str.replace(frase, ".", " ")
    frase = str.replace(frase, ";", " ")
    frase = str.replace(frase, "!", " ")
    frase = str.replace(frase, "?", " ")
    
    return frase 

def inverte(frase):
    
    str.split(retira_pontuacao(frase))