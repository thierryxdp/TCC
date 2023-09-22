def retira_pontuacao(frase):
    """Funcao que dada uma frase retorna a mesma com todos os caracteres de pontuacao substituidos por espaço; str-> str"""
    frase = frase
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('-',')
    return frase