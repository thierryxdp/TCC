def inverte(frase):
    '''funcao que inverte um frase dada como
    parametro.
    entrada: string
    saida: string
    '''
    f0= frase.lower()
    f1= f0.replace('-', ' ')
    f2= f1.replace(',', ' ')
    f3= f2.replace(':', ' ')
    f4= f3.replace(';', ' ')
    f5= f4.replace('!', ' ')
    f6= f5.replace('?', ' ')
    f7= f6.replace('.', ' ')
    frase_formada= f7.split()
    inversao= frase_formada[::-1]
    return " ".join(inversao)