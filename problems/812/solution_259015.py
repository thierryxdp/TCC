def retira_pontuacao(frase):
    """retorna a frase substituindo todos caracteres de pontuação por espacos em branco"""
    frase= frase.replace('!',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace('-',' ')