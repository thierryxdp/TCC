def retira_pontuacao(frase):
    '''retorna a frase onde os caracteres de pontuacao
    sao substituidos por espaco; str->str'''
    frase=str.replace(frase, '-',' ')
    frase=str.replace(frase, '-',' ')
    frase=str.replace(frase, ':',' ')
    frase=str.replace(frase, ',',' ')
    frase=str.replace(frase, '?',' ')
    frase=str.replace(frase, '!',' ')
    frase=str.replace(frase, '.',' ')
    frase=str.replace(frase, '...',' ')
    return  frase