def retira_pontuacao(frase):
    """Retorna a frase onde todos os caracteres de pontuação são substituídos por espaço
    entrada: str"""
    return frase.replace("."," ").replace("!"," ").replace("?"," ").replace(","," ").replace(";"," ").replace("_"," ").replace("-"," ")
def inverte(frase):
    y=str.join("",reversed(str.split(frase)))
    return (str.lower(y))