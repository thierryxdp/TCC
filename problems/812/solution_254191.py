def retira_pontuacao(frase):
    """essa função recebe uma frase de entrada e substitui os caracteres de pontuação da frase por espaços;
    string ->string"""
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    return frase