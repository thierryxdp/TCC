def retira_pontuacao(frase):
    """função que dada uma frase, retorne ela com suas pontuações substituidas poe espaço; str-->str"""
    frase=frase.replace("-"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace("."," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase
def inverte(frase):
    """função que dada uma frase, retorne uma nova frase com as mesmas palavras que a anterior, de trás pra frente, sem pontuação e sem letras maiusculas; str-->str"""
    frase= frase.lower()
    frase= frase.split()
    nova_frase=list(range(frase))-1
    return nova_frase + retira_pontuacao(frase)