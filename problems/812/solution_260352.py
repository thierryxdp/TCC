def retira_pontuacao(frase):
    '''retira as pontuaçoes da frase de entrada
    str->str'''
    
    texto= str.replace(frase,['-','.',',',':',';','!','?'],'')
    return texto