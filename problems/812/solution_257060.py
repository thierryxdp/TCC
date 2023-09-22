def  retira_pontuacao(frase):
    '''funcao que dada uma frase, retorne a frase onde todos os caracteres de
pontuacao (incluindo travessao, virgula, dois pontos, ponto e virgula, alem da
pontuacao de encerramento de frase) são substituidos por espaço
    str -> str'''
    
    sub=frase.replace('–',' ')
    sub=sub.replace(',',' ')
    sub=sub.replace(':',' ')
    sub=sub.replace(';',' ')
    sub=sub.replace('.',' ')
    sub=sub.replace('-',' ')

    return sub