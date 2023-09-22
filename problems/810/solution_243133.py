def retira_pontuacao(frase):
    """função que retira pontuações de uma frase
    str=>str"""
    frase_nova = frase.replace("-"," ").replace(","," ").replace(":"," ").replace("."," ").replace(";"," ").replace("?"," ").replace("!"," ")
    return frase_nova

def inverte(frase):
    
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    frase_final = str.split(frase)
    return list.reverse(frase_final)