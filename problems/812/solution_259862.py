def retira_pontuacao(frase):
    '''funcao que retira a pontuacao dada
    uma frase.
    entrada: string
    saida: string
    '''
    f1= frase.replace('-', ' ')
    f2= f1.replace(',', ' ')
    f3= f2.replace(':', ' ')
    f4= f3.replace(';', ' ')
    f5= f4.replace('!', ' ')
    f6= f5.replace('?', ' ')
    f7= f6.replace('-', ' ')
    frase_formada= f7.split()
    inversao= frase_formada[::-1]
    return " ".join(inversao)