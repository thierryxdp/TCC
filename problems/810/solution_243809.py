def retira_pontuacao(frase):
    """função que retira pontuações de uma frase
    str=>str"""
    frase_nova = frase.replace("-"," ").replace(",","").replace(":","").replace(".","").replace(";","").replace("?","").replace("!","")
    return frase_nova

def inverte(frase):
    """Função que inverte as palavras de uma 
    frase, retirando pontuação e sem letras maiúsculas
    str=>str"""
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase_final = frase.split(" ")
    fraseF = frase_final[::-1]
    return " ".join(fraseF).lstrip()