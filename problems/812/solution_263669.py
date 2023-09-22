import re
def retira_pontuacao(frase):
    """Retire todas as pontuações da frase inicial e substitua por um espaço"""
    return re.sub(',|!|?|.|/|:|;' , frase)