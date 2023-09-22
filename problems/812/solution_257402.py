def retira_pontuacao(frase):
    """ dada um frase qualquer vamos retirar todas as pontuações e retornaremos
        a frase
        entrada --> str
        saida   --> str   """
    frase = frase.replace("-"," ")
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase = frase.replace(";"," ")
    frase = frase.replace("."," ")
    frase = frase.replace("?"," ")
    frase = frase.replace("!"," ")
    return frase


""" teste
    resultados esperados:
    resultados obtidos: """