def inverte(frase):
    """ Essa função, dada uma frase, retorna uma outra frase que contem as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.

        Parameters:
        frase = frase a ser inserida e avaliada

        Testes:
            

        Returns:
            frase que contem as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
            str --> str
    """
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,",","")
    frase = str.replace(frase,":","")
    frase = str.replace(frase,";","")
    frase = str.replace(frase,":","")
    frase = str.replace(frase,"...","")
    frase = str.replace(frase,".","")
    frase = str.replace(frase,"!","")
    frase = str.replace(frase,"?","")
    lista = str.split(frase," ")
    lista = lista[::-1]
    resultado = str.join(" ",lista)
    resultado = str.lower(resultado)
    return resultado