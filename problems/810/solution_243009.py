def retira_pontuacao(frase):
    """função que retira pontuações de uma frase
    str=>str"""
    frase_nova = frase.replace("-"," ").replace(","," ").replace(":"," ").replace("."," ").replace(";"," ").replace("?"," ").replace("!"," ")
    return frase_nova
def inverte(phrase):
    fraseF = retira_pontuacao(phrase)
    fraseF = str.lower(phrase)
    return fraseF[::-1]