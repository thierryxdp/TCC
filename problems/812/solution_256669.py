def retira_pontuacao(frase):
    x = str.replace(frase,"."," ")
    y = str.replace(frase,"?"," ")
    z = str.replace(frase,"!"," ")
    
    if "!" in frase:
        return z 
    elif "." in frase:
        return x