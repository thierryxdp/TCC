def lingua_p(palavra:str)->str:


    """ Função que dado uma palavra em português, traduz e retorna a palavra para
        o idioma P.
        P: Idioma P é quando, após cada vogal da palavra original,
        é inserida a sequência de letras p mais a vogal original.

    """

    vogais = "AEIOUaeiouãâáéêíîõóôûúÂÃÁÉÊÌÎÔÕÓÚÛ"
    nova_palavra = palavra

    for ps in range(len(palavra)):

        if palavra[ps] in vogais:

            novo =  palavra[ps] + p

            nova_palavra = str.replace(nova_palavra,palavra[ps],novo)

    return nova_palavra