def inverte(frase):
    
    for dados in frase:

        for dado in ''''-.?![]":,''':

            frase = frase.replace(dado, '')
    
    frase = frase.split()

    frase.reverse()

    frase = str(frase)

    for dado in ''' '-.?![]": ''':

        frase = frase.replace(dado, '')

    for dado in ',':

        frase = frase.replace(dado, ' ')
    
    return frase.lower()