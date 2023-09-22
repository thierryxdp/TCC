def retira_pontuação (frase):
    """dada uma frase, função retorna a frase onde todos os caracteres
    de pontuação são substituídos por espaço"""
    """string -> string"""
    frase = frase.replace('-', '')
    frase = frase.replace(',', '')
    frase = frase.replace(':', '')
    frase = frase.replace(';', '')
    frase = frase.replace('.', '')
    frase = frase.replace('!', '')
    frase = frase.replace('?', '')
    return frase