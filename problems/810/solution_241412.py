from math import*
def inverte(frase):
    """Dado uma frase, função retorna uma outra frase que contém as mesmas
    palavras da frase de entrada na ordem inversa"""

    auxiliar= frase.replace('.',' ')
    auxiliar= auxiliar.replace('...',' ')
    auxiliar= auxiliar.replace('?',' ')
    auxiliar= auxiliar.replace('!',' ')
    auxiliar= auxiliar.replace(':',' ')
    auxiliar= auxiliar.replace(',',' ')
    auxiliar= auxiliar.replace(';',' ')
    auxiliar= auxiliar.replace('-',' ')

    auxiliar= str.lower(auxiliar)

    listaAuxiliar= auxiliar.split(' ')
    contadora= len(listaAuxiliar)
    fraseInvertida= listaAuxiliar[contadora - 1::-1]
    fraseInvertida= ' '.join(fraseInvertida)
    

    return fraseInvertida