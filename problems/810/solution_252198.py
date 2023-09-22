#retira pontuacao de uma frase
def retira_pontuacao (frase):
    novafrase = str.replace (frase, ",", "")
    novafrase = str.replace (novafrase, ".", "")
    novafrase = str.replace (novafrase, "-", " ")
    novafrase = str.replace (novafrase, "!", "")
    novafrase = str.replace (novafrase, "?", "")
    novafrase = str.replace (novafrase, ";", "")
    novafrase = str.replace (novafrase, ":", "")
    return novafrase
        
#Retira maiuscula
def retira_maiuscula (novafrase):
    novafrase1 = novafrase.lower()
    return novafrase1
    
#inverte
def inverte1 (novafrase1):
    novafrase2 = novafrase1.split()
    novafrase2.reverse()
    return novafrase2

def inverte (frase):
    frasesemPontuacao = retira_pontuacao(frase)
    frasesemPontuacaoeMinuscula = retira_maiuscula(frasesemPontuacao)
    fraseInvertida = inverte1(frasesemPontuacaoeMinuscula)
    return " ".join(fraseInvertida)