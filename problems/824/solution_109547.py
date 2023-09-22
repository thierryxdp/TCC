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

    for palavra in frase:
        if palavra in "bcdfghjklmnpqrstvwxzy":
            palavra = str.upper(palavra)
        nova = nova + palavra

    return nova