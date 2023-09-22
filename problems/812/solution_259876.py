def retira_pontuacao(texto):
    frase_final = texto
    frase_final = frase_final.replace("...",".")
    frase_final = frase_final.replace("-"," ")
    frase_final = frase_final.replace(","," ")
    frase_final = frase_final.replace(":"," ")
    frase_final = frase_final.replace("."," ")
    frase_final = frase_final.replace(";", " ")
    frase_final = frase_final.replace("?"," ")
    frase_final = frase_final.replace("!"," ")
    return frase_final