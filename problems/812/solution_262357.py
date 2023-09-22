def retira_pontuacao (frase):
    """Insira a frase entre aspas e a funcao retornara a frase sem nenhuma pontuação"""
    """str=>str'''
    frase=frase.replace("."," ")
    frase=frase.replace("/"," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(","," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase