def retira_pontuacao(frase):
    """função que dada uma frase, retorna ela com suas pontuações substituidas por espaço; str-->str"""
    frase= frase.replace("-"," ")
    frase= frase.replace(","," ")
    frase= frase.replace(":"," ")
    frase= frase.replace(";"," ")
    frase= frase.replace("."," ")
    frase= frase.replace("!"," ")
    frase= frase.replace("?"," ")
    return frase