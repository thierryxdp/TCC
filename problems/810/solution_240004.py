def retira_pontuacao(frase):
    frase = frase.replace('!', ' ')
    frase1 = frase.replace('-', ' ')
    frase2 = frase1.replace(',', ' ')
    frase3 = frase2.replace(':', ' ')
    frase4 = frase3.replace(';', ' ')
    frase5 = frase4.replace('.', ' ')
    frase6 = frase5.replace('?', ' ')
    return frase6

def inverte(frase):
    frase = retira_pontuacao(frase).lower()
    lista = frase.split()
    num = -1
    num.join('', lista)