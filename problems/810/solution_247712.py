def retira_pontuacao(texto):
    '''função dado uma frase remove todas pontuações
    str--->str'''
    frase = str.replace(texto,'-',' ')
    frase = str.replace(texto,',',' ')
    frase = str.replace(texto,':',' ')
    frase = str.replace(texto,';',' ')
    frase = str.replace(texto,'.',' ')
    frase = str.replace(texto,'?',' ')
    frase = str.replace(texto,'!',' ')
    return frase
def inverte(frase):
    '''função que inverte o sentido de uma frase sem suas pontuacoes
    str--->str'''
    frase = retira_pontuacao(frase)
    frase = str.split(frase)
    return frase[::-1]