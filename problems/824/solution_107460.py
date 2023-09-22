def uppCons(frase:str) -> str:
    """Função torna as consoantes da frase maiusculas

       frase:
       numeros: frase a ser analisada

       Return:
       frase com apenas as consoantes maiusculas
    """
    i = 0

    while i < len(frase):
        if frase[i] in not 'AEIOUaeiou':
            frase[i] = str.upper(frase[i])
        i = i + 1
    return frase