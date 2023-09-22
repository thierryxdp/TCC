def uppCons(frase):

    '''Devolve a frase dada na mesma frase mas com todas as consoantes maiúsculas'''

    # str -> str

    consoantesM = 'BCÇDFGHJKLMNPQRSTVWXYZ'
    consoantes = 'bcçdfghjklmnpqrstvwxyz'

    conso = []

    for letra in frase:

        if letra in consoantes[0:]:

            letra = letra.upper()

            conso.append(letra)

    return frase