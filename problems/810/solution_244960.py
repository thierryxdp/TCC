def retira_pontuacao(frases):
    '''função que retorna um frase retirando todos os caracteres de pontuação: str => str'''
    frases = frases.replace("."," ")
    frases = frases.replace("/"," ")
    frases = frases.replace(";"," ")
    frases = frases.replace(","," ")
    frases = frases.replace(":"," ")
    frases = frases.replace("-"," ")
    frases = frases.replace("?"," ")
    frases = frases.replace("!"," ")
    return frases

def inverte(frases):
    '''função que inverte a ordem das palavras da frase, assim retornando um frase alterada; str => str'''
    frases.reverse()
    return frases