# Função que inverte uma frase, retirando a pontuação e as letras maiúsculas
# periodo é uma frase qualquer 
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
def inverte(frase):
    """Função que inverte uma frase, retirando a sua pontuação e suas letras maiúsculas"""
    "str->str"""
    list.reverse(list(frase))
    return frase