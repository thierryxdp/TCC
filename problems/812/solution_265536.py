def retira_pontuacao(frase):
    frase=frase.replace(";"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("!"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("."," ")
    return frase
'''funcao que dada uma frase retorna a mesma frase onde todos os carcteres de pontuacao sejam substituidos por espaco.
entrada:str
saida:str'''