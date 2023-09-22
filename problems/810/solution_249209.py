def retira_pontuacao(frase):
    '''funcao que dada uma frase retorne uma frase onde todos os caracteres de pontuação sejam substituidos por espaço
    str->str'''
    str.join(frase," ")
    return frase.replace(':',' ').replace(',',' ').replace('.',' ').replace('-',' ').replace('!',' ').replace('?',' ')
def inverte(frase):
    '''função que retorna a frase invertida da frase dada como parametro 3
    str->str'''
    listafrase = str.spl(retira_pontuacao)
    return str.join(' ' , listafrase)