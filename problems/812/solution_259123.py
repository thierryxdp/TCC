def retira_pontuacao(frase):
    """Recebe uma frase e retorna a mesma sem pontuacao"""
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    return frase