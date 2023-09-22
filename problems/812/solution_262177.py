def retira_pontuacao(frase):
    
    
    
    novo1 = frase.replace(",", "",1)
    
    novo2 = frase.replace(".", "",2)
    
    return (novo1, novo2)