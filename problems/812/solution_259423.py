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
    frase= str.split(frase)
    frase= frase[::1]
    frase= str.join(' ',(frase))
    frase= str.lower(frase)
    return frase