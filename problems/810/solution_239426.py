def retira_pontuacao(frase):
    """Retorna a frase onde todos os caracteres de pontuação são substituídos por espaço
    entrada: str"""
    return frase.replace("."," ").replace("!"," ").replace("?"," ").replace(","," ").replace(";"," ").replace("_"," ").replace("-"," ")
def inverte(frase):
    x=retira_pontuacao(frase)
    y=x.split()
    inverte= str.join("",y[::-1])
    return str.lower(inverte)