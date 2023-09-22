def retira_pontuacao(frase):
    '''função dado uma frase remove todas pontuações
    str--->str'''
    frase += str.replace(frase,'-',' ')
    frase += str.replace(frase,',',' ')
    frase += str.replace(frase,':',' ')
    frase += str.replace(frase,';',' ')
    frase += str.replace(frase,'.',' ')
    return frase