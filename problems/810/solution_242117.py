def inverte(frase):
    '''retira as pontuaçoes da frase de entrada
    str->str'''
    
    travessao= str.replace(frase,'-',' ')
    virgula=str.replace(travessao,',',' ')
    dois_pontos=str.replace(virgula,':',' ')
    ponto_virgula=str.replace(dois_pontos,';',' ')
    exclamacao=str.replace(ponto_virgula,'!',' ')
    interrogacao=str.replace(exclamacao,'?',' ')
    ponto=str.replace(interrogacao,'.',' ')
    
    minuscula=str.lower(ponto)
    separa=str.split(minuscula)
    return str.join(separa[::-1])