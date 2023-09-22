def retira_pontuacao(frase):
    '''retira as pontuaçoes da frase de entrada
    str->str'''
    
    travessao= str.replace(frase,'-',' ')
    virgula=str.replace(travessao,',',' ')
    dois_pontos=str.replace(virgula,':',' ')
    ponto_virgula=str.replace(dois_pontos,';',' ')
    exclamacao=str.replace(ponto_virgula,'!',' ')
    interrogacao=str.replace(exclamacao,'?',' ')
    ponto=str.replace(interrogacao,'.',' ')
    
    return ponto

def minuscula(retira_pontuacao(frase)):
    '''passa todos os caracteres para minuscula'''
    return str.lower(frase)

def inverte(minuscula(retira_pontuacao)):
    '''inverte a frase de entrada)
    str->str'''
    return str.partition(minuscula,'')