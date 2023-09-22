def retira_pontuacao(frase):
    
    novo1 = frase.replace("-", "")
    novo2 = frase.replace(",", "")
    novo3 = frase.replace(":", "")
    novo4 = frase.replace(";", "")
    
    return (novo1 + novo2 + novo3 + novo4)