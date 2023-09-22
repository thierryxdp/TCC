def retira_pontuacao(frase): 
    '''Faça uma função que, dada uma frase, retorne a frase onde todos os caracteres de pontuação tenham
sido substituidos por espaço'''
    #str > str
    pont = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for i in frase:
        if i in pont:
             frase = frase.replace(i, " ")
    return frase