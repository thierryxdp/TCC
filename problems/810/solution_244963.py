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

def inverte(frase):
    '''função que inverte a ordem das palavras da frase, assim retornando um frase alterada; str => str'''
    retira_pontuacao = frase.reverse()
    return frase