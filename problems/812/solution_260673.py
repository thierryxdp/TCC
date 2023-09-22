def retira_pontuacao(frase):
    '''dada uma string, retorna a mesma sem as pontuações
str-->str'''
    return str.strip(frase,"-,:;.!?")