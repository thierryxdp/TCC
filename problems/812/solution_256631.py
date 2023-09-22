def retira_pontuacao(frase):
    '''função que dada uma frase, substitui a pontuação por um espaço vazio '''
    frase = str.replace(frase,","," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"/"," ")
    return frase