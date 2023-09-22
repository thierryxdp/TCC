#retorna a frase onde todas as pontuações foram substituidas por espaços
def retira_pontuacao(texto):
    texto = texto.replace("-"," ")
    texto = texto.replace(","," ")
    texto = texto.replace(":"," ")
    texto = texto.replace(";"," ")
    texto = texto.replace ("?"," ")
    texto = texto.replace("."," ")
    texto = texto.replace("!"," ")
    return texto