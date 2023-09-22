def retira_pontuacao(frase):
    '''retorna frase sem pontuacao'''
    frase=frase.replace(".","")
    frase=frase.replace("/","")
    frase=frase.replace(";","")
    frase=frase.replace(",","")
    frase=frase.replace(":","")
    frase=frase.replace("-","")
    frase=frase.replace("?","")
    frase=frase.replace("!","")
    return frase