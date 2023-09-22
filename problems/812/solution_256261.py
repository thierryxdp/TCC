def retira_pontuacao(frase): 
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for i in frase:
        if i in punc:
             frase = frase.replace(i, " ")
    return frase