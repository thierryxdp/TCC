def inverte(frase):
    '''funcao que inverte um frase dada como
    parametro.
    entrada: string
    saida: string
    '''
    minusculo= frase.lower()
    remover1= minusculo.replace(',', ' ')
    remover2= remover1.replace('.', ' ')
    frase_formada= remover2.split()
    inversao= frase_formada[::-1]
    return " ".join(inversao)