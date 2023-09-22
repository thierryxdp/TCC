def lingua_p1(palavra):
    """ Essa função recebe uma palavra e depois de cada vogal
    é inserida a letra p, e transforma todas as as letras 
    maiusculas em minusculas. 
    
    assinatura: string---> string"""
    texto_minusculo = palavra.lower()
    lista_texto = list(texto_minusculo)
    frase_p = []
    for letra in lista_texto:
        if letra in 'aeiouáàéíóú':
            frase_p = frase_p + list(letra) + list('p') + list(letra)
        else:
            frase_p = frase_p + list(letra)
    frase_p = (''.join(frase_p))
    return frase_p