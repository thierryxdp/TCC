def uppCons(frase):
    """
    Essa função modifica todos as consoantes minisculas para maisculas
    de uma frase.
    Parametros de entrada: string
    Valor de retorno: string
    """

    i = 0
    f1 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(f1, str.upper(frase[i]))
        else:
            list.append(f1, frase[i])
        i = i + 1
    return str.join("", f1)