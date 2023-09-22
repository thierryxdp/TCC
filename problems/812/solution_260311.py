def retira_pontuacao(frase):
    '''retira as pontuaçoes da frase de entrada
    str->str'''
    
   
    dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)

    return dataClean