def retira_Pontuacao(texto):
    texto = str.replace(texto, "-"," ")
    texto = str.replace(texto, ","," ")
    texto = str.replace(texto, ":"," ")
    texto = str.replace(texto, ";"," ")
    texto = str.replace(texto, "."," ")
    texto = str.replace(texto, "?"," ")
    texto = str.replace(texto, "!"," ")
    texto = str.replace(texto, "..."," ")
    
    return texto