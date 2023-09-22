def uppCons(frase):

    '''Devolve a frase dada na mesma frase mas com todas as consoantes maiúsculas'''

    # str -> str

    consoantesM = 'BCÇDFGHJKLMNPQRSTVWXYZ'
    consoantes = 'bcçdfghjklmnpqrstvwxyz'

    fraseM = str.maketrans(consoantes,consoantesM)

    return frase.translate(fraseM)