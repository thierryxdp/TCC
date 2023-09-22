def uppCons(string):
    """Recebe uma frase e retorna a mesma com as consoantes em letras maiúsculas, mantendo o
    restante na forma original.
    assinatura: str --> str
    casos de teste:
    uppCons('belo dia para nadar')==(BeLo Dia PaRa NaDaR)
    """
    vogal=['a', 'e', 'i', 'o', 'u']
    filtro=[x.upper() if x not in vogal else x for x in string]
    filtro
    return filtro