def retira_pontuacao(frase):
    pontos = [".",","]
    frase2 = str.replace(frase, pontos," ")
        
    return frase2