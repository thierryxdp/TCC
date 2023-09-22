def inverte(frase):
    """ Essa função, dada uma frase, retorna uma outra frase que contem as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.

        Parameters:
        frase = frase a ser inserida e avaliada

        Testes:
            inverte("que fazia tudo!") = "que fazia tudo " 
            inverte("Oh!") = "Oh "
            inverte("Anda apanhar um capotinho, Capitu, dizia-lhe ele.") = "Anda apanhar um capotinho  Capitu  dizia lhe ele "

        Returns:
            frase que contem as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
            str --> str
    """
    frase = str.replace(frase,"-","")
    frase = str.replace(frase,",","")
    frase = str.replace(frase,":","")
    frase = str.replace(frase,";","")
    frase = str.replace(frase,":","")
    frase = str.replace(frase,"...","")
    frase = str.replace(frase,".","")
    frase = str.replace(frase,"!","")
    frase = str.replace(frase,"?","")
    lista = str.split(frase," ")
    lista2 = lista[::-1]
    resultado = str.join(" ",lista2)
    resultado = str.lower(resultado)
    return resultado