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
    
    frase_separada = str.split(retira_pontuacao(frase))
    
    frase_invertida = frase_separada[::-1]
    
    return str.join (" frase_invertida ")