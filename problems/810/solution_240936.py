def inverte(frase):
    '''funcao que inverte um frase dada como
    parametro.
    entrada: string
    saida: string
    '''
    remover= frase.replace(',', ' ')
    frase_formada= remover.split()
    inversao= frase_formada[::-1]
    return " ".join(inversao)