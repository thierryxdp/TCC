def retira_pontuacao(texto):
    " Função que dado uma texto, retprna o texto sem as pontuações. str--> str"
    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,";"," ")
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,","," ")    
    texto = str.replace(texto,"!"," ")
    texto = str.replace(texto,"?"," ")
    texto = str.replace(texto,":"," ")
    return texto