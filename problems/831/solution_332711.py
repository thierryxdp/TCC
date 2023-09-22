def lingua_p(palavra):
    """
    Essa função modifica a palvra para a linguagem do 'P'.
    Após cada vogal da palavra ooriginal, é inserida a sequência 
    de letras 'p' mais a vogal original
    Parametro de entrada: str
    Valor de retorno: str
    """
    p = ''
    minu = str.lower(palavra)
    
    for letra in minu:
        if letra in "AEIOUaeiouáéíóú":
            letra = letra + 'p' + letra
        p = p + letra
    return p