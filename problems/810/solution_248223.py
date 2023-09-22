def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    return frase.replace(","," ").replace("/"," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")

def inverte(frase):
    """Inverta a frase de entrada sem os sinais de pontuação"""
    frase= retira_pontuacao(frase)
    return list.reverse(frase)