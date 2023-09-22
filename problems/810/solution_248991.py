def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    return frase.replace(","," ").replace("/"," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")
def inverte(frase):
    """Retorne a frase de entrada sem os sinais de pontuação, com as letras minúsculas e a frase invertida"""
    
    nova=str.lower(retira_pontuacao(frase))
    return nova[::-1]