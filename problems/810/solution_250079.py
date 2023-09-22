def  inv_phrase ( frase ):
    """função que dá uma frase restitui uma outra frase que sabe
        as mesmas palavras da frase de entrada na ordem inversa."""
    lista  =  str . dividir ( frase )
    lista . reverso ()
    #lista = list.reverse(lista)
    frase  =  str . join ( " " , lista )
     frase de retorno