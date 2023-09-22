'''função que determina a quantidade de frases em um texto, separando essas frases depois de suas respectivas pontuações
str->int'''
def conta_frases(texto):
    a=len(str.partition(texto,".","?","...","!"))
    return a