def inverte(frase):
    '''funcao que dada uma frase, retorna uma outra na ordem inversa sem pontuacao ou letra maiuscula;
    str-> str'''
    frase= str.replace(frase, '-', ' ')
    frase= str.replace(frase, ',', ' ')
    frase= str.replace(frase, ':', ' ')
    frase= str.replace(frase, ';', ' ')
    frase= str.replace(frase, '.', ' ')
    frase= str.replace(frase, '?', ' ')
    frase= str.replace(frase, '!', ' ')
    frase= str.lower(frase)
    return frase[::-1]