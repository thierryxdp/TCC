def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    nova_frase =[frase]
    return nova_frase.replace(","," ").replace("/"," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")

def inverte(frase):
    """Inverta a frase de entrada sem os sinais de pontuação"""
    retira_pontuacao(frase) = [frase]
    
    return list.reverse(retira_pontuacao(frase))