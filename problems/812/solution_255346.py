def retira_pontuação (frase):
    """dada uma frase, função retorna a frase onde todos os caracteres
    de pontuação são substituídos por espaço"""
    """string -> string"""
    frase1 = frase.replace('-', ' ')
    frase2 = frase1.replace(',', ' ')
    frase3 = frase2.replace(':', ' ')
    frase4 = frase3.replace(';', ' ')
    frase5 = frase4.replace('.', ' ')
    frase6 = frase5.replace('!', ' ')
    frase7 = frase6.replace('?', ' ')
    return frase7