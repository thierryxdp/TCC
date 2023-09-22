def inverte(frase):
    '''dada uma frase a função inverte a ordem das palavras, as colocando de
    trás para frente e retirando a pontuação'''

    palavras=str.split(frase," ")
    return str.join(" ",palavras[::-1]).lower().replace("!","").replace("?","").replace("...","").replace(".","").replace("-","").replace(":","").replace(";","").replace(",","")