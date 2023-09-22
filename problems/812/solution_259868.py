def retira_pontuacao(frase):
    """Função que retira a pontuaçao de uma frase(-,:,;,.,!,? e ","),
retornando a frase sem essas pontuações, trocando-as por espaço;
String, String->String"""
    frase=frase.replace('-',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    return frase