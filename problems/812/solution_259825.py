def retira_pontuacao(frase):
    '''funcao que retira a pontuacao dada
    uma frase.
    entrada: string
    saida: string
    '''
    pontuacao1= frase.split(',')
    pontuacao2= frase.split('.')
    pontuacao3= frase.split('!')
    pontuacao4= frase.split('?')
    retira= pontuacao1, pontuacao2, pontuacao3, pontuacao4
    return " ".join(retira)