def retira_pontuacao(frase):
    """função que retira pontuações de uma frase
    str=>str"""
    frase_nova = frase.replace("-"," ").replace(","," ").replace(":"," ").replace("."," ").replace(";"," ").replace("?"," ").replace("!"," ")
    return frase_nova

def inverte(frase):
    
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase_final = frase.split(" ")
    fraseF =frase_final[::-1]
    return " ".join(fraseF).lstrip()