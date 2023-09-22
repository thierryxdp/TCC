def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    nova_frase =[frase]
    return nova_frase.replace(","," ").replace("/"," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")

def inverte(frase):
    """Inverta a frase de entrada sem os sinais de pontuação"""
    frase = nova_frase
    return list.reverse(frase)