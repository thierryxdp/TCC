def retira_pontuacao(frase):
    """
    	Retorna a frase sem nenhum caractere de pontuação, substiuindo-o por espaço.
        str -> str
    """
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    return frase