#Funçao que retira pontuaçao da frase e substitui por espaços
#str -> str
def retira_pontuacao(frase):
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    return frase