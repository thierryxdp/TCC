def retira_pontuacao(frase):
    
    
    
    i = frase.find(",")
    novo1 = frase.replace(",", "")  
    j = frase.find(".")
    novo2 = frase.replace(".", "")
    
    return (novo1, novo2)