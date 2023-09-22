#Exercício_03:
''' Essa função recebe uma frase, uma letra e um número e tetorna o índice
    em que se encontra a letra em sua determinada repetição. '''
''' str, strm int ---> int. '''

def  posLetra(string, letter, number):
    nc = str.count(string, letter)
    if nc < number:
        return (-1)
    else:
        c=number-1
        z= str.replace(string, letter, "@", c)
        r=str.index(z, letter)
        return r