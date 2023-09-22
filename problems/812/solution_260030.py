def retira_pontuacao(frase):
    """Recebe uma string e retira a pontuação dessa.
    string -> string"""
    corrigida = frase.replace('-', ' ')
    corrigida = frase.replace(',', ' ')
    corrigida = frase.replace(':', ' ')
    corrigida = frase.replace(';', ' ')
    corrigida = frase.replace('.', ' ')
    corrigida = frase.replace('...', ' ')
    corrigida = frase.replace('!', ' ')
    corrigida = frase.replace('?', ' ')
    return corrigida