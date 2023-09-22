def retira_pontuacao(frases):
    '''função que retorna um frase retirando todos os caracteres de pontuação: str => str'''
    frases = frases.replace(".","")
    frases = frases.replace("/","")
    frases = frases.replace(";","")
    frases = frases.replace(",","")
    frases = frases.replace(":","")
    frases = frases.replace("-","")
    frases = frases.replace("?","")
    frases = frases.replace("!","")
    return frases