def retira_pontuacao(frase):
    
    
    
    i = frase.find(",")
    novo1 = frase.replace(",", "",[0:i])  
    j = frase.find(".")
    novo2 = frase.replace(".", "",[0:j])
    
    return (novo1, novo2)