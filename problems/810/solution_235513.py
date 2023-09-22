def retira_pontuacao(frase):
    return frase.replace('.', ' ').replace('?', ' ').replace('!', ' ').replace(',', ' ').replace('-', ' ').replace(':', ' ').replace(':', ' ').replace(';', ' ').replace('...', ' ')

def inverte(frase):
    lista_resultado = retira_pontuacao(frase).lower().split()[::-1]
    return ' '.join(lista_resultado)