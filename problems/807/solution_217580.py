'''função que determina a quantidade de frases em um texto, separando essas frases depois de suas respectivas pontuações
str->int'''
def conta_frases(texto):
    pontuações=".","...","!","?"
    a=len(str.partition(texto,"pontuações"))
    return a