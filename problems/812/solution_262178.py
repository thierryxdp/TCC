def retira_pontuacao(frase):
    
    
    
    i = frase.find(",")
    novo1 = frase.replace(",", "",i)  
    j = frase.find(".")
    novo2 = frase.replace(".", "",j)
    
    return (novo1, novo2)