def inverte(frase):
    '''função que dada uma frase retorna uma outra frase que 
     contenha as mesmas palavras da frase de entradada na ordem iversa,
     sem letras maiúsculas, e sem a pontuação; str -> str'''
    frase= str.split(frase)
    frase.reverse()
    frase= str.join(" ", frase)
    return frase