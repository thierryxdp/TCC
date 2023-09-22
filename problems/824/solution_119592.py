def uppCons (frase):
    """Dada uma frase, retorna a mesma com as consoantes em maiúsculo
    assinatura: str -> str
    testes:
    """
    i = 0
    consoante = ''
    while i < len (frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            str.upper(i)
            consoante = frase[i]
            i += 1
    return consoante