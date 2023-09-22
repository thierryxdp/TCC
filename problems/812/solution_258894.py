# Dada uma frase, retorna a frase substituindo caracteres de pontuação em espaço.
# string -> string
def retira_pontuacao(frase):
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ')