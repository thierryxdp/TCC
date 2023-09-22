def retira_pontuacao (frase):
'''funcao que retorna frase sem pontuacao'''
'''str=>str'''
frase=frase.replace("."," ")
frase=frase.replace("/"," ")
frase=frase.replace(";"," ")
frase=frase.replace(",","  frase=frase.replace(":"," ")
    frase=frase.replace("-"," ")
    frase=frase.replace("?"," ")
    frase=frase.replace("!"," ")
    return frase
def inverte (frase):
    frase = frase.split()
    frase = list(reversed(frase))
    retira_pontuacao()
    return (" ".join(frase))