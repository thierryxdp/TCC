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
    """função que dada uma frase, retorne uma nova frase com as mesmas palavras que a anterior na ordem inversa, sem pontuação e sem letrasmaiusculas; str-->str"""
    frase= retira_pontuacao(frase)
    str.lower(frase)
    str.split(frase)
    nova_frase= ""frase.join(frase[::-1])
    return nova_frase