def retira_pontuacao(texto):
    '''função dado uma frase remove todas pontuações
    str--->str'''
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    return frase
def inverte(frase):
    '''função que inverte o sentido de uma frase sem suas pontuacoes
    str--->str'''
    frase = retira_pontuacao(frase)
    frase = str.split(frase)
    return frase[::-1]