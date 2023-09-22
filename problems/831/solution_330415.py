def lingua_p(palavra):
    """
    	Função que traduz a palavra dada para linguagem do
        P.
        string -> string
    """
    retorno = ''
    for letras in palavra:
        if letra in 'AEIOUaeiou':
            letra = letra + 'p' + letra
        retorno = retorno + letra
    return retorno