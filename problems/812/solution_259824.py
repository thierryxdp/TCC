def retira_pontuacao(frase):
    '''funcao que retira a pontuacao dada
    uma frase.
    entrada: string
    saida: string
    '''
    retira= frase.split(" ")    
    return " ".join(retira)