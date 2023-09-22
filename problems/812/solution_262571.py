# Retira a pontuação
# periodo
# str->str
def retira_pontuacao(periodo):
    """Função que dada a str de entrada substitui a potuação por espaços"""
    """str->str"""
    frase=periodo
    frase=frase.replace("."," ")
    frase=frase.replace(","," ")
    frase=frase.replace(";"," ")
    frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase