#Funçao que retira pontuaçao da frase e substitui por espaços
#str -> str
def retira_pontuacao(frase):
    frase.replace('-',' ')
    frase.replace(',',' ')
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace('.',' ')
    return frase