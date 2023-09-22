def retira_pontuacao(frase):
    """essa função recebe uma frase qualquer e, usando a função replace() substitui as pontuações por espaços;
    str->str"""
    frase= frase.replace('!',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace(',',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    return frase