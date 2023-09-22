def retira_pontuação (frase):
    """dada uma frase, função retorna a frase onde todos os caracteres
    de pontuação são substituídos por espaço"""
    """string -> string"""
    frase = str.replace(frase,'-', '')
    frase = str.replace(frase',', '')
    frase = str.replace(frase':', '')
    frase = str.replace(frase';', '')
    frase = str.replace(frase'.', '')
    frase = str.replace(frase'!', '')
    frase = str.replace(frase'?', '')
    return frase