retira_pontuacao(frase):
    
    a = str.replace(frase, "-", " ") 
    b = str.replace(frase, ",", " ")
    c = str.replace(frase, ":", " ")
    d = str.replace(frase, ";", " ")
    e = str.replace(frase, ".", " ")