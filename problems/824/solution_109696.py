def uppCons(frase: str) -> str:
    """Dada uma frase, retorna essa frase com todas as consoantes dessa frase
       maiúsculas

       Parameters:
       frase: Frase qualquer na forma de string

       Return:
       Dado o parâmetro "frase", retorna a string do parâmetro com todas as
       consoantes maiúsculas

       Examples:
       uppCons("bc") == 'BC'
       uppCons("oi, como você está?") == 'oi, CoMo VoCê eSTá?'
       uppCons("oi") == 'oi'
    """

    nova = ""
    i = 0

    while i < len(frase):
        if frase[i] in "bcdfghjklmnpqrstvwxzyç":
            letra = str.upper(frase[i])
        else:
            letra = frase[i]
        nova = nova + letra
        i = i + 1

    return nova