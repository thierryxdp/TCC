def retira_pontuacao(frase):
    '''Esta e a funcao que dada uma frase, retorna
    a frase onde todos os caracteres de pontuacao são 
    substituidos por espaco
    str -> str'''
    a='.'
    b='-'
    c=','
    d=':'
    e=';'
    for a in frase:
        frase.replace(a,'')
        frase.replace(b,'')
        frase.replace(c,'')
        frase.replace(d,'')
        frase.replace(e,'')
        return frase