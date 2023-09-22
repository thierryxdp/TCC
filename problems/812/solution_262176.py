def retira_pontuacao(frase):
    
    novo1 = frase.replace(",", "")
    novo2 = frase.replace(".", "")
    
    return (novo1, novo2)