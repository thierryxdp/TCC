def retira_pontuacao(frase):
    """Retorna a frase onde todos os caracteres de pontuação são substituídos por espaço
    entrada: str"""
    return frase.replace("."," ").replace("!"," ").replace("?"," ").replace(","," ").replace(";"," ").replace("_"," ").replace("-"," ")
def inverte(frase):
    x=str.split(frase[::-1])
    y=str.join(string,x)
    return retira_pontuacao(str.lower(y))