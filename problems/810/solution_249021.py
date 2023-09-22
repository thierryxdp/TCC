def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    return frase.replace(","," ").replace("/"," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")

def inverte(frase):
    """Inverta a frase de entrada, excluindo os sinais de pontuação e colocando todas as letras minúsculas"""
    
    str.lower(retira_pontuacao(frase))
    nova = [retira_pontuacao(frase)]
    return str.join(list.reverse(nova))