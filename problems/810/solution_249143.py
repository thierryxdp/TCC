def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    return frase.replace(","," ").replace("/"," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")

def diminui(frase):
    """Retorne a frase com letra minúscula"""
    return str.lower(retira_pontuacao(frase))
def inverte(frase):
    """Inverta a frase de entrada"""
    lista = str.split(diminui(frase))
    list.reverse(lista)
    return str.join(' ',lista)