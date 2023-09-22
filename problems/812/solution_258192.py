def retira_pontuacao(frase):
   """funcao que troca todas as pontuacoes por espaco"""
   """ string->string"""
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace("."," ")
    return frase