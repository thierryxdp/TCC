def lingua_p(palavra):
    """Funcao que dada uma palavra em portugues retorna esta palavra
    traduzida na lingua do P.
    Obs: Na lingua do apos cada vogal é inserido P mais a vogal
    str --> str"""
    P = ""
    for i in range(len(palavra)):
        x = str.lower(palavra)
        if palavra[i] in "aáàâãeéêiíîoóôõuú": 
            P = P + palavra[i] + "p" + palavra[i]
        else:
            P = P + palavra[i]
    return P