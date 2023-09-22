def inverte(frase):
    '''Função que,dada uma frase, retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
    str -> str'''
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.lower(frase)
    frase = str.split(frase)
    frase.reverse()
    frase str.join(' ', frase)
    return frase
 
lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return phrase