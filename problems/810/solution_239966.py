# Dada uma frase, retorna a frase substituindo caracteres de pontuação em espaço.
# string -> string
def retira_pontuacao(frase):
    return frase.replace('-', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ')

# Dada uma frase, retorna ela com a posição das palavras invertidas
# string -> string
def inverte(frase):
    frase = retira_pontuacao(frase).lower()
    frase = frase.split(' ')[::-1]
    return str.strip(str.join(' ', frase))