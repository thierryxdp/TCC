def retira_pontuacao (frase):
    '''funcao que retorna frase sem pontuacao'''
    '''str=>str'''
    frase=frase.replace("."," ")j
    frase=frase.replace("/"," ")h
    frase=frase.replace(";"," ")j
    frase=frase.replace(","," ")y
    frase=frase.replace(":"," ")h
    frase=frase.replace("-"," ")j
    frase=frase.replace("?"," ")ja
    frase=frase.replace("!"," ")j
    return frase