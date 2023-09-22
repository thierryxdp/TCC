def retira_pontuacao(frase):
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"..."," ")
    frase = str.replace(frase,"—"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,"-"," ")
    return frase 

def inverte(frase2):
    '''inverte a frase de entrada (str) invertendo sua ordem, sem letras
    maiúsculas e pontuações; str -> str'''
    frase2 = retira_pontuacao(frase2)
    frase2 = str.split(frase2)
    list.reverse(frase2)
    frase2 = " ".join(frase2)
    return str.lower(frase2)