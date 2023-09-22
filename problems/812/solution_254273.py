def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço.
    str->str"""
    frase=frase.replace('?', ' ')
    frase=frase.replace('!', ' ')
    frase=frase.replace('-', ' ')
    frase=frase.replace('.', ' ')
    frase=frase.replace(',', ' ')
    return frase