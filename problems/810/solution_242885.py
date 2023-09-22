def inverte(frase):
    """ funcao que dada uma frase retorne uma outra frase
       que contenha as mesmas palavras da frase de entrada 
       na ordem inversa """
    lista = lista.reverse( )
    frase = frase.join(" ", lista)
    return frase
    
    
    
    
   
    lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return phrase