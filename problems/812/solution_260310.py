def retira_pontuacao(frase):
    '''retira as pontuaçoes da frase de entrada
    str->str'''
    
    dataClean = ''.join(data).lower()

    dataClean = re.sub(r'["-,.:@#?!&$]', ' ', dataClean)

    return dataClean)