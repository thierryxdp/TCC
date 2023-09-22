# Dada uma frase, retorna a frase substituindo travessão, vírgula, dois pontos,
# ponto e vírgula, e ponto, em espaço.
# string -> string
def retira_pontuacao(frase):
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ')