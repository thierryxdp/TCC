def retira_pontuacao(frase):
    """funcao que retorna a frase de entrada str --> str"""
    frase=frase.replace('.','')
    frase=frase.replace('...','')
    frase=frase.replace('?','')
    frase=frase.replace('!','')
    frase=frase.replace('-','')
    frase=frase.replace('_','')
    frase=frase.replace(';','')
    frase=frase.replace(':','')
    frase=frase.replace(',','')
    return frase